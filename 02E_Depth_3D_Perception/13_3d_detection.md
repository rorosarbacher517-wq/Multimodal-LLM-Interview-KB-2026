# 3D Detection：PointPillars / SECOND / CenterPoint

## 输出

3D detector 常输出：

`[x, y, z, w, l, h, yaw, class, score]`

## PointPillars

```text
points
→ pillarize XY
→ pillar features
→ pseudo-image BEV
→ 2D CNN detector
```

优点：快。

## SECOND

把点云 voxelize，再用 sparse 3D convolution 提取几何特征。

## CenterPoint

在 BEV 上把 3D object 看成中心点检测，再回归 size、yaw、velocity 等。

## 面试重点

3D detection 的难点不是只多一个 z，而是 coordinate system、sparse input、orientation 和 temporal motion。