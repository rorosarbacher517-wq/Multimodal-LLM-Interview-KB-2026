# 03 · Multimodal Core Architecture

## Q1. 一个典型 MLLM 的底层结构是什么？

```text
Image / Video
   ↓
Vision Encoder
[B,N,Dv]
   ↓
Projector / Resampler
[B,N',Dl]
   ↓
Visual Tokens + Text Tokens
[B,L,Dl]
   ↓
LLM
   ↓
Text / Coordinates / Tool Call / Action
```

核心只有两个问题：**把视觉变成 LLM 能读的表示；让这种表示保留足够信息但又不太贵。**

## Q2. 为什么需要 Projector？

Vision Encoder 的 hidden size `Dv` 通常与 LLM `Dl` 不一样，不能直接拼接。

最简单：

```text
[B,N,Dv] → Linear/MLP → [B,N,Dl]
```

Projector 既做维度映射，也学习视觉语义到语言表示空间的适配。

## Q3. MLP Projector 为什么这么常见？

- 参数少；
- 训练稳定；
- 不增加复杂 cross-attention；
- 当 vision encoder、LLM 和数据足够强时，简单连接器常已能达到很好效果。

它的缺点是通常不会主动减少 token 数。

## Q4. Q-Former 是怎么工作的？

给定大量视觉特征 `[B,N,Dv]`，引入固定数量 `K` 个 learnable queries：

```text
K queries --cross-attention--> N visual tokens
→ K compressed visual tokens
```

因此同时实现：

- 信息选择；
- token 压缩；
- 视觉语言对齐。

代价是结构和训练更复杂。

## Q5. Perceiver Resampler / Resampler 做什么？

本质与 Q-Former 类似：用一组 latent/query 通过 cross-attention 把可变长度视觉特征压到受控长度。

适合：

- 高分辨率图像；
- 多图；
- 视频；
- 需要稳定 LLM token budget 的场景。

## Q6. Projector 和 Token Compressor 是一回事吗？

不完全是。

- Projector 重点解决 `Dv → Dl`；
- Compressor 重点解决 `N → N'`；
- 一个模块可以同时做两件事，但概念上应分开。

面试画 shape 时要分别说明**特征维度**和**序列长度**如何变化。

## Q7. Early Fusion、Late Fusion、Cross-Attention 怎么理解？

- **Early/token fusion**：视觉 token 早早进入统一序列，与文本共同 self-attention。
- **Cross-attention fusion**：语言 hidden state 通过额外 cross-attention 读取视觉 K/V。
- **Late fusion**：两个模态先独立建模，在较后层融合。

没有绝对最好，区别是交互深度、计算成本和模块化程度。

## Q8. LLaVA 路线为什么影响很大？

它把 MLLM 简化成：

```text
CLIP-like Vision Encoder
→ simple projector
→ LLM
```

再配合大规模视觉指令数据完成 alignment + instruction tuning。意义在于证明：不一定需要复杂 adaptor，数据和强 backbone 也能构建强 VLM。

## Q9. Flamingo 路线与 LLaVA 最大区别？

Flamingo 使用视觉 Resampler，并在语言模型层间插 gated cross-attention；LLaVA 更倾向把视觉 token 直接映射后拼进 LLM 序列。

所以：

- Flamingo：视觉 memory 被文本 cross-attend；
- LLaVA：视觉 token 成为统一上下文的一部分。

## Q10. BLIP-2 的核心价值？

BLIP-2 用 Q-Former 在冻结视觉编码器和冻结 LLM 之间建立信息瓶颈，证明可以用较少可训练参数完成高效视觉语言对齐。

面试重点不是背训练任务，而是理解：**learnable queries 从视觉中抽取固定长度的语言相关信息。**

## Q11. Native Resolution 到底是什么意思？

不是“原图每个像素原封不动进模型”。更准确地说：模型不强制把所有输入压成同一个固定低分辨率，而是根据原始尺寸/长宽比构造视觉 token。

仍然会存在：patchify、resize、tile、merge、token budget。

## Q12. 动态分辨率为什么是 2026 面试重点？

它直接连接三个方向：

1. **能力**：OCR/GUI/文档需要细节；
2. **模型**：视觉 token 如何生成和压缩；
3. **系统**：token 多了会增加 prefill、KV/cache、显存。

因此它不是纯视觉预处理问题，而是 end-to-end design 问题。

## Q13. 多图输入怎么组织？

通常每张图分别编码，再按对话顺序插入：

```text
[text] [image1 tokens] [text]
[image2 tokens] [text] ...
```

需要额外处理：

- image index / separator；
- 总视觉 token budget；
- 不同尺寸 padding/packing；
- 跨图 reference，例如“第二张图左边的人”。

## Q14. 视频为什么不能只理解成很多图片？

视频多了三个核心问题：

- 时间顺序；
- 跨帧对象持续性；
- 事件发生的起止时间。

简单逐帧编码可以作为 baseline，但高质量视频理解还需要 temporal position、timestamp alignment、帧选择/压缩。

## Q15. 多模态位置编码与文本位置编码有什么不同？

文本是 1-D 序列；图像天然是 `(H,W)`；视频是 `(T,H,W)`。

因此多模态 RoPE/position scheme 需要把空间和时间位置映射到 attention。模型还要处理“文本 token 和视觉 token 在统一序列中的相对顺序”。

## Q16. 为什么多层视觉特征融合有用？

最后一层更偏高级语义，中间层保留更多局部细节。把多个层级的视觉特征送入/融合到 LLM，可同时改善：

- OCR；
- spatial reasoning；
- fine-grained recognition；
- grounding。

但会增加带宽、token 或额外 projection 成本。

## Q17. MLLM 的 loss 一定包含 image reconstruction 吗？

不一定。最常见理解型 VLM 可以只通过语言 next-token loss 学视觉能力：

```text
image → visual tokens
prompt + visual tokens → predict answer tokens
```

视觉 encoder/projector 的梯度来自文本生成 loss。统一理解+生成模型才可能再加入 image tokenizer/diffusion/generative objective。

## Q18. 如何评价一个新的 MLLM 架构设计？

不要只看 benchmark。按 6 个维度：

1. **Perception**：分辨率、vision backbone；
2. **Compression**：每张图多少 token；
3. **Fusion**：视觉什么时候进入 LLM；
4. **Reasoning**：SFT/RL 怎么做；
5. **Efficiency**：prefill、KV、MoE、部署；
6. **Capability coverage**：OCR、grounding、video、agent 是否真的训练过。

这套框架可以用来分析几乎所有新模型。