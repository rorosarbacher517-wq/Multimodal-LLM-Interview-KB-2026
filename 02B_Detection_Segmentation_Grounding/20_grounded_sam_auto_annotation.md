# Grounded SAM / Grounded SAM 2 为什么重要？如何做自动标注？

## 核心组合

```text
Text prompt
   ↓
GroundingDINO / DINO-X
   ↓ boxes
SAM / SAM 2
   ↓ masks
Open-vocabulary segmentation / tracking
```

Grounding model 负责“找到对象”，SAM 负责“把对象切准”。两者通过 box/point prompt 自然衔接。

## 视频版 Grounded SAM 2

- 关键帧先做 text grounding。
- box/mask prompt 初始化 SAM 2 object state。
- 后续帧用 streaming memory 传播目标。
- 目标丢失或新增对象时再重新 grounding。

## 自动标注流水线

```text
Raw images
 → concept vocabulary
 → GroundingDINO boxes
 → SAM masks
 → score/area/overlap filtering
 → human spot-check
 → COCO/YOLO labels
 → train fast YOLO student
 → online hard cases → next data round
```

这是一条非常实用的 **teacher → pseudo label → student → bad-case loop**。

## Primary sources

- https://arxiv.org/abs/2401.14159
- https://github.com/IDEA-Research/Grounded-SAM-2
