# 02 · Vision Fundamentals

## Q1. CNN 和 ViT 的核心区别？

- CNN 有局部卷积核、平移等变等强 inductive bias，天然高效建模局部纹理。
- ViT 把图像转成 patch token，再用 Transformer 建模全局关系。
- ViT 在大规模预训练下更容易扩展，并与 LLM 的 token-based 架构天然兼容。

## Q2. 图像如何变成 ViT token？

输入 `[B,3,H,W]`，patch size 为 `P`：

```text
N = (H/P) × (W/P)
[B,3,H,W]
→ patchify
→ [B,N,3P²]
→ Linear
→ [B,N,Dv]
```

实际模型还可能加入 CLS token、2D position encoding、patch merge 或动态 resize。

## Q3. Patch size 越小越好吗？

不是。

- 小 patch：细节更好，token 更多，计算更贵；
- 大 patch：token 少，但容易丢小目标、OCR、细粒度信息。

因此高分辨率 MLLM 的核心问题不是单纯减小 patch，而是**动态分辨率 + token compression/routing**。

## Q4. ViT 的 position embedding 为什么是视觉能力关键？

视觉 token 不仅要知道内容，还要知道 `(x,y)`。如果模型只知道 patch 内容，不知道位置，就很难做 spatial relation、grounding、图表和 GUI。

处理不同分辨率时，绝对 position embedding 还可能需要插值，因此现代 MLLM 更常采用可扩展的二维/多维位置方案。

## Q5. CLIP 是怎么训练的？

CLIP 用 image encoder 和 text encoder 把图文映射到同一 embedding space，用对比学习：

- 正样本：匹配的 image-text；
- 负样本：batch 内其他组合；
- 优化目标：正确图文相似度高，错误组合低。

CLIP 学到的是很强的语义表征，因此常作为早期 VLM 的视觉塔。

## Q6. Contrastive Learning 为什么适合视觉语言对齐？

它不要求逐像素标签，只要海量图文配对，就能让视觉语义与语言语义进入同一空间，数据扩展性强。

缺点是全局 embedding 容易弱化细粒度空间信息，所以 grounding/OCR 仍需额外数据和训练。

## Q7. SigLIP 相对 CLIP 的重要变化是什么？

核心思想之一是用 sigmoid-based pairwise loss，而不是必须依赖 batch 内全局 softmax 归一化。这使训练在大 batch/分布式设置下更灵活。SigLIP/SigLIP2 视觉编码器在现代轻量 VLM 中非常常见。

## Q8. DINO / DINOv2 为什么对多模态有价值？

DINO 系列通过 self-supervised teacher-student 学习，无需文本监督，也能得到很强的视觉结构和局部表征。

与 CLIP 相比：

- CLIP 更强语言语义对齐；
- DINO 更强调纯视觉结构与局部 correspondence。

一些模型会组合或选择更适合 downstream 的视觉 backbone。

## Q9. Vision Encoder 到底输出了什么？

通常不是“识别后的标签”，而是连续特征：

```text
[B,N,Dv]
```

每个 token 对应一个 patch/region 的高维表示。深层 token 偏语义，较浅/中层特征往往保留更多局部细节。

## Q10. 为什么只用 ViT 最后一层可能损失细节？

越深的层越倾向形成任务相关的高级语义和不变性，小纹理、边缘、精确位置可能被弱化。

因此一些新 VLM 会：

- 使用多层特征；
- skip/stack features；
- 高低层融合；
- 特殊 token compressor 保留局部细节。

## Q11. OCR 为什么特别依赖高分辨率？

小文字在低分辨率 resize 后可能只剩几个像素。即使 LLM 再强，也无法恢复输入中已经消失的信息。

OCR 的链路是：

**视觉采样质量 → 字符局部特征 → layout/reading order → 文本语义推理。**

## Q12. Grounding 和普通 VQA 有什么区别？

VQA 只要求回答“是什么”；grounding 还要求回答“在哪里”。输出可能是：

- bbox `[x1,y1,x2,y2]`；
- point `(x,y)`；
- region mask；
- coordinate tokens。

Grounding 是 GUI Agent、具身控制、视觉工具调用的基础能力。

## Q13. Detection / Segmentation 模型和 MLLM 的关系？

传统 detector/segmenter 擅长精确空间输出；MLLM 擅长开放词汇理解和推理。

实际系统常组合：

```text
MLLM 负责理解/规划
→ detector/SAM 负责精确定位
→ MLLM 继续推理/行动
```

不是所有视觉任务都应该强行让 LLM 自己输出像素级结果。

## Q14. 为什么动态分辨率比固定 224×224 更适合 MLLM？

真实输入可能是：手机截图、超长 PDF、横向表格、4K 图片。固定 resize 会严重扭曲或丢失细节。

动态分辨率会根据原始长宽比、任务和 token budget 选择 resize/tile，使模型在细节和成本之间折中。

## Q15. Tile-based 高分辨率处理有什么问题？

优点：保留细节。

问题：

- tile 数量增加导致视觉 token 爆炸；
- 同一个物体可能被切断；
- 需要全局缩略图帮助恢复整体布局；
- tile 顺序和位置必须编码清楚。

## Q16. 视觉模型常见错误如何定位？

建议分四层：

1. **Input**：resize/crop 是否已经丢信息？
2. **Encoder**：局部特征是否能区分目标？
3. **Alignment**：visual token 是否被 LLM 正确利用？
4. **Reasoning**：视觉证据正确，但推理过程出错？

面试中能把错误拆开，比只说“增加训练数据”更有价值。