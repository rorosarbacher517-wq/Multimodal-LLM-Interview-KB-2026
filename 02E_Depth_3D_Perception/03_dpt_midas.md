# DPT / MiDaS：Transformer Depth 基础

## 面试一句话

DPT 把 ViT 的 global token representation 重组回 dense spatial prediction，使 Transformer 能用于 depth/segmentation 这类逐像素任务。

## Pipeline

```text
image
→ ViT tokens at multiple layers
→ reassemble to feature maps
→ multi-scale fusion
→ dense depth map [B,1,H,W]
```

## MiDaS 路线

通过多数据集混合训练提升 cross-dataset relative depth 泛化。

## 为什么是后续 foundation depth 的基础

强预训练视觉 encoder + dense decoder 的模式后来在 Depth Anything 等模型中继续发展。

## Reference

- DPT: https://arxiv.org/abs/2103.13413