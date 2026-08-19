# 02A · Vision Backbones & Visual Pretraining

> `02 Vision Fundamentals` 负责“图像为什么能变成特征”；本模块进一步回答：**为什么视觉 backbone 从 ResNet 走到 ViT/Swin/ConvNeXt，预训练又从 supervised 走到 CLIP/DINO/MAE/SigLIP2。**

---

## Part A. CNN Backbone

### Q1. CNN 的核心 inductive bias 是什么？
- locality：卷积核只看局部；
- weight sharing：同一 kernel 扫整张图；
- translation equivariance：输入平移，feature 也相应平移。

这使 CNN 在中小数据和实时视觉任务中依然非常高效。

### Q2. ResNet 最重要的贡献是什么？
Residual block 学：

```text
H(x) = x + F(x)
```

信息和梯度可以沿 identity path 更直接传播，使非常深的网络更容易优化。

### Q3. Bottleneck Block 为什么用 `1×1 → 3×3 → 1×1`？
先压通道，再做昂贵 3×3，再升通道，从而减少计算，同时保留表达能力。

### Q4. Feature Pyramid 为什么重要？
浅层分辨率高、定位细；深层语义强、分辨率低。检测、分割需要同时利用不同尺度。

### Q5. ConvNeXt 为什么值得懂？
它把现代 Transformer 时代的训练/结构经验重新带回纯 CNN，例如更大 kernel、depthwise conv、LayerNorm 风格设计等，说明 CNN 与 ViT 的差异并不是“卷积已经过时”。

---

## Part B. ViT / Hierarchical Transformer

### Q6. ViT 与 CNN 最本质的表示差异？
CNN 保留 `[B,C,H,W]` feature map；ViT 常把 patch flatten 成：

```text
[B,N,D]
```

再通过 self-attention 让任意 patch 交互。

### Q7. CLS Token 是什么？
额外添加一个 learnable token，让它在 Transformer 中汇聚全局信息，最后用于分类/全局 embedding。

但不是所有视觉模型都必须用 CLS；也可以 mean pooling。

### Q8. CLS Pooling 和 Mean Pooling 怎么选？
- CLS：专门学习全局聚合。
- Mean：平均所有 patch token。

没有理论上绝对赢家，取决于预训练目标和 backbone 实现。

### Q9. Swin Transformer 为什么用 Window Attention？
全局 attention 对高分辨率 `N²` 太贵。Swin 只在局部窗口 attention，并通过 shifted windows 让不同窗口跨层交流。

### Q10. 为什么 Swin 是 Hierarchical Backbone？
它逐阶段降低空间分辨率、增加通道，形成类似 CNN 的多尺度 feature hierarchy，因此很适合 detection/segmentation。

### Q11. Position Embedding 插值为什么会出现？
ViT 预训练时可能是固定 grid，例如 `14×14`。下游换更大 grid 时，绝对位置 embedding 数量不匹配，需要 2D interpolation。

这也是 dynamic-resolution 模型偏好更灵活位置编码的原因。

---

## Part C. Supervised / Self-supervised / Contrastive Pretraining

### Q12. Supervised ImageNet Pretraining 的作用？
先用大规模分类任务学习通用视觉特征，再 fine-tune 下游。

缺点是 label space 有限，无法直接得到语言对齐。

### Q13. MAE 的核心思想？
随机 mask 大部分 image patches，仅根据可见 patches 重建被 mask 的内容。

它把“遮住再预测”从 NLP 引入视觉，适合规模化 self-supervised representation learning。

### Q14. 为什么 MAE 可以 mask 很高比例？
自然图像空间冗余很大，相邻区域高度相关；同时只把可见 token 送 encoder，可以显著降低预训练计算。

### Q15. DINO / DINOv2 在学什么？
Teacher-student self-distillation，让不同视角/增强下的同一图像得到一致、结构化表示，不依赖文本标签。

其 patch features 往往有很好的局部 correspondence 和 segmentation-like structure。

### Q16. CLIP 和 DINO 的信息来源不同在哪里？
- CLIP：图像和自然语言对齐，语义开放性强。
- DINO：纯视觉 self-supervision，局部视觉结构强。

现代视觉塔常需要在“语言语义”和“空间细节”之间权衡。

### Q17. SigLIP 为什么改变 CLIP 的 batch 依赖？
CLIP 常使用 batch 内 global softmax contrastive objective；SigLIP 用 pairwise sigmoid loss，使训练不必把所有 pair 放进一个全局 softmax。

### Q18. SigLIP2 为什么值得多模态岗位关注？
它在语言对齐之外进一步强化 localization、dense features、多分辨率/多语言等视觉能力，因此很适合作为现代 VLM vision encoder 候选。

回答具体模型细节时应回官方论文/model card，而不是只凭“SigLIP2”名字推断。

---

## Part D. Augmentation / Input Processing

### Q19. Resize、Center Crop、Random Crop 会改变什么？
它们不只是工程预处理，也在定义模型看见的视觉分布。错误 resize 可能直接毁掉小字、长宽比和空间结构。

### Q20. 常见 Data Augmentation 为什么能提高泛化？
通过 color jitter、flip、crop、RandAugment/Mixup/CutMix 等人为增加输入变化，减少模型记忆训练样本细节。

但 OCR/图表/医学等任务不能盲目使用会改变标签语义的增强。

### Q21. Image Normalization 在做什么？
按通道减均值/除标准差，把输入数值范围调整到 backbone 预训练时的分布。

换 vision encoder 时 processor 的 mean/std 也要一起换。

### Q22. 为什么 Processor 是模型的一部分？
实际输入 token 数由 resize、tile、patch merge、mean/std、frame sampling 等共同决定。

只下载权重但 processor 配错，模型能力会显著下降。

---

## Part E. Dense Feature 与 MLLM

### Q23. Global Embedding 和 Dense Patch Feature 区别？
- global embedding `[B,D]`：适合 retrieval/classification。
- dense features `[B,N,D]` / `[B,C,H,W]`：保留空间信息，适合 grounding/OCR/segmentation/MLLM。

### Q24. 为什么 MLLM 不能只接一个 CLIP Global Vector？
一个 global vector 压缩太强，精确位置、小字、多对象关系很容易丢失。现代 MLLM 通常保留大量 patch/region tokens。

### Q25. 为什么多层视觉特征融合越来越常见？
中层保留纹理/位置，最后层更语义化。多层融合可以补细节，但增加 feature bandwidth 和 connector 复杂度。

### Q26. 选择 Vision Backbone 时应该看什么？
不要只看 ImageNet accuracy。至少看：
1. input resolution；
2. patch/stride；
3. dense feature quality；
4. language alignment；
5. OCR/grounding；
6. compute/token 数；
7. 是否易于 fine-tune/serve。

## Primary references
- ResNet: https://arxiv.org/abs/1512.03385
- ViT: https://arxiv.org/abs/2010.11929
- Swin: https://arxiv.org/abs/2103.14030
- ConvNeXt: https://arxiv.org/abs/2201.03545
- MAE: https://arxiv.org/abs/2111.06377
- DINOv2: https://arxiv.org/abs/2304.07193
- CLIP: https://arxiv.org/abs/2103.00020
- SigLIP: https://arxiv.org/abs/2303.15343
