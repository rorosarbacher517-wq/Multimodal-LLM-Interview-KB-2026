# 01 · Transformer & LLM Fundamentals

> 目标：不是背 Transformer，而是能从 shape、复杂度、显存和现代 LLM 改进一路讲到多模态。

## Q1. 为什么 Transformer 取代 RNN 成为大模型主干？

**一句话：** Transformer 用注意力直接建立任意 token 之间的联系，同时训练阶段可以并行处理整个序列。

- RNN 的依赖路径随距离增长，而且训练按时间步递归，难并行。
- Self-Attention 中任意两个 token 的信息路径长度接近常数级。
- 代价是标准 attention 对序列长度 `L` 的计算/中间注意力矩阵近似 `O(L²)`。
- 对 MLLM，图像/视频会增加大量视觉 token，所以 `L²` 问题更明显。

## Q2. Q、K、V 到底是什么？

输入 `X ∈ R^{B×L×D}`：

```text
Q = XWq
K = XWk
V = XWv
Attention(Q,K,V)=softmax(QK^T/sqrt(d))V
```

直观理解：

- **Q**：当前 token 想找什么信息；
- **K**：每个 token 用什么特征让别人匹配自己；
- **V**：匹配成功后真正传递的内容。

注意：Q/K/V 都是从隐藏状态线性投影出来的连续向量，不是“单词字典”。

## Q3. 为什么要除以 `sqrt(d_k)`？

若 Q、K 各维方差近似 1，点积方差会随维度 `d_k` 增大。值过大会让 softmax 过度饱和，梯度变小。除以 `sqrt(d_k)` 把数值尺度拉回更稳定范围。

## Q4. Multi-Head Attention 为什么需要多头？

一个头只能在一个投影子空间中计算相似度。多头允许不同头学习不同关系，例如局部、句法、实体、长距离依赖。

典型 shape：

```text
[B,L,D]
→ [B,L,H,d]
→ transpose
→ [B,H,L,d]
```

其中 `D = H × d`。

## Q5. Self-Attention 和 Cross-Attention 区别？

- Self-Attention：Q/K/V 都来自同一个序列。
- Cross-Attention：Q 来自一个序列，K/V 来自另一个序列。

多模态中：

- LLaVA 类常把视觉 token 和文本 token 拼成一个序列后做 self-attention；
- Flamingo 类用文本 query 对视觉 K/V 做 cross-attention；
- Q-Former 则用 learnable queries 对视觉特征做 cross-attention。

## Q6. Causal Mask 是什么？

Decoder-only 模型训练 next-token prediction 时，第 `t` 个位置不能看到未来 token。做法是在 attention logits 上给未来位置加 `-∞`，softmax 后权重变 0。

多模态中视觉 token 通常作为上下文先出现，因此后续文本 token 可以读取视觉信息。

## Q7. 为什么现代 LLM 大多是 Decoder-only？

- 训练目标统一：next-token prediction；
- 生成任务与预训练形式一致；
- 数据组织简单，容易规模化；
- prompt、工具结果、多模态 token 都可以组织成一个上下文序列。

Encoder-only 更适合理解/表征，Encoder-Decoder 对翻译等 seq2seq 很自然，但通用生成式 foundation model 更常用 Decoder-only。

## Q8. LayerNorm 和 RMSNorm 有什么区别？

LayerNorm 同时减均值、除标准差；RMSNorm 主要按均方根缩放，不做减均值。

```text
RMS(x)=sqrt(mean(x²)+eps)
y = x / RMS(x) * gamma
```

RMSNorm 更简单，现代 LLM 中非常常见。

## Q9. Pre-Norm 为什么比 Post-Norm 更适合深层 Transformer？

Pre-Norm 把 normalization 放在 attention/FFN 前，残差主干更像一条稳定的 identity path，深层训练通常更容易优化。Post-Norm 在非常深的网络里更容易出现梯度不稳定。

## Q10. FFN 为什么通常比 Attention 参数更多？

标准 FFN：`D → D_ff → D`，而 `D_ff` 通常是 `D` 的数倍。现代模型常用 SwiGLU：

```text
SwiGLU(x) = (SiLU(xW1) ⊙ xW2) W3
```

FFN 可以理解为逐 token 的非线性特征变换；Attention 主要负责 token 之间的信息路由。

## Q11. RoPE 是什么？为什么流行？

RoPE 对 Q/K 的二维分量做随位置变化的旋转，使点积自然包含相对位置信息。

优势：

- 不需要单独把位置向量直接加到 hidden state；
- 相对位置关系容易进入 attention；
- 能与长上下文扩展策略配合；
- 可以推广到多维位置，例如图像 H/W、视频 T/H/W。

## Q12. MHA、MQA、GQA 区别？

- **MHA**：每个 Q head 都有自己的 K/V head。
- **MQA**：所有 Q heads 共用一组 K/V。
- **GQA**：若干 Q heads 共用一组 K/V，是折中方案。

GQA 主要价值在 decode：减少 K/V heads 后，KV cache 和内存读取显著降低。

## Q13. KV Cache 为什么能加速自回归生成？

生成第 `t` 个 token 时，过去 token 的 K/V 不会改变，因此缓存起来，下一步只计算新 token 的 Q/K/V。

近似显存：

```text
B × L × n_layers × n_kv_heads × head_dim × 2(K,V) × bytes
```

长上下文、多图、视频都会把 `L` 拉大，所以多模态 serving 特别关心 KV cache。

## Q14. Prefill 和 Decode 的瓶颈为什么不同？

- **Prefill**：一次处理整个 prompt，矩阵乘大，通常更偏 compute-bound。
- **Decode**：每一步只有少量新 token，但反复读取模型权重和 KV cache，常更偏 memory-bandwidth-bound。

视觉 token 主要把 prefill 拉长；长生成主要把 decode 拉长。

## Q15. MoE 的核心思想是什么？

把 FFN 换成多个 expert，由 router 为每个 token 选择 top-k experts。

```text
x → router scores → top-k experts → weighted sum
```

关键区分：

- **Total parameters**：所有专家加起来；
- **Active parameters**：一个 token 实际激活的参数。

MoE 增加容量而不让每个 token 都跑全部参数，但带来路由负载均衡和 all-to-all 通信。

## Q16. MoE 的 load balancing 为什么重要？

如果大量 token 都路由到少数专家：

- 热门 expert 过载；
- 其他 expert 学不到东西；
- 分布式 all-to-all 出现严重 straggler。

因此通常需要 auxiliary load-balancing loss、capacity control 或更稳定的 routing 设计。

## Q17. Dense Attention、Sliding Window、Linear/Recurrent Attention 怎么比较？

- Dense Attention：全局能力强，但长序列贵。
- Sliding Window：只看局部窗口，成本随窗口近似线性增长，但跨远距离信息受限。
- Linear/Recurrent 类：通过状态或核技巧避免显式 `L×L` attention，长上下文更高效，但表达方式和缓存机制不同。
- 2026 的一些模型开始使用 **hybrid architecture**：部分层保留 full attention，其他层用更高效的 recurrent/linear 模块。

## Q18. 为什么多模态算法岗也必须懂 LLM 推理结构？

因为视觉最终常变成 token 进入 LLM。你优化：

- 图像分辨率；
- 视觉 token 压缩；
- 多图/视频长度；
- projector；

本质都会改变 LLM 的序列长度、prefill、KV cache 和显存。所以“视觉模型结构”和“LLM 系统”不能分开准备。