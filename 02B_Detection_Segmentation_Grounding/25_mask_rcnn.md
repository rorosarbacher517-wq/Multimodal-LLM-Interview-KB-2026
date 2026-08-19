# Mask R-CNN 为什么经典？

Mask R-CNN 在 Faster R-CNN 的 box/classification branch 之外增加并行 mask branch。

```text
Backbone/FPN
   ↓
RPN proposals
   ↓
RoIAlign
 ├─ class
 ├─ box
 └─ mask
```

## RoIAlign 为什么重要？
避免 RoIPool 的坐标量化误差，用双线性插值获得更精确的区域特征，对像素级 mask 尤其重要。

## 局限
两阶段结构精度强但 pipeline 较复杂、实时性通常不如轻量 one-stage segmentation。
