# SAM 的底层结构和维度怎么变化？

## 面试一句话

SAM = **Image Encoder + Prompt Encoder + Mask Decoder**。图像只需重编码一次，之后 point/box/mask prompt 可以复用同一 image embedding。

## 官方默认维度

```text
Image [B,3,1024,1024]
   ↓ ViT patch_size=16
64×64 visual grid
   ↓ neck / out_chans=256
Image embedding [B,256,64,64]

Point / Box → sparse prompt embeddings
Mask        → dense prompt embedding

Image embedding + prompts
   ↓ Two-Way Transformer
mask logits + predicted IoU
```

## 核心点

- ViT-B/L/H 的 encoder hidden size 和 depth 不同。
- Prompt embedding 维度统一为 256。
- Mask decoder 使用 Two-Way Transformer，让 prompt 与 image feature 双向交互。
- SAM 是 promptable segmentation，不是文本 open-vocabulary detector；文本通常需要 GroundingDINO 等模型先转成 box/point。

## Primary sources

- https://github.com/facebookresearch/segment-anything/blob/main/segment_anything/build_sam.py
- https://arxiv.org/abs/2304.02643
