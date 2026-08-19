# SfM / Bundle Adjustment 在做什么

## SfM

Structure from Motion 从多张有重叠的图像恢复：

- camera intrinsics/extrinsics；
- sparse 3D points。

## 传统 Pipeline

```text
feature detection
→ feature matching
→ relative pose / essential matrix
→ triangulation
→ incremental reconstruction
→ bundle adjustment
```

## Bundle Adjustment

联合优化 camera parameters 和 3D points，使重投影误差最小：

`min Σ || project(P_j, X_i) - x_ij ||²`

## 为什么重要

传统 SfM 强但 pipeline 长、匹配和初始化敏感。DUSt3R/VGGT 等学习式方法正是在尝试减少这些手工步骤。