# DETR / Hungarian Matching / Deformable DETR / DINO 怎么串起来？

## DETR

DETR 把检测写成**集合预测**：一组 object queries 输出一组 boxes/classes，再与 GT 做 Hungarian one-to-one matching。

```text
Image features
   ↓ Transformer encoder
Object queries
   ↓ decoder
Q predictions
   ↓ Hungarian matching
GT objects
```

## 为什么原始 DETR 难训？

- 全局 attention 成本高。
- 收敛慢。
- 小目标、多尺度表现有限。

## Deformable DETR

围绕 reference points 只采样少量关键位置，并直接使用 multi-scale features，因此更高效、更适合小目标。

## DINO Detector

DINO 在 DETR 路线上继续改进 denoising training、anchor/query initialization 等机制。

## 易错点

**DINO detector ≠ DINOv2。** 前者是目标检测器；后者是自监督 ViT 视觉 backbone。GroundingDINO 中的 DINO 指 detector 路线。
