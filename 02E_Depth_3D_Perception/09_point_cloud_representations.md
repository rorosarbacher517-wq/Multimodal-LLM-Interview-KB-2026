# Point Cloud：Point / Voxel / Pillar / Range View

## Raw Points

`[N, C]`，常见 `C = xyz + intensity + timestamp...`

优点：不量化；缺点：无规则、GPU 计算困难。

## Voxel

把 3D 空间离散成网格。规则但很多 voxel 是空的，因此常用 sparse convolution。

## Pillar

只在 XY 平面划格，Z 方向压成柱子，PointPillars 代表这种高效路线。

## Range View

把 LiDAR 投影到按 azimuth/elevation 排列的 2D 图，更像 image CNN。

## 面试重点

表示方式决定后续计算结构：Point Transformer、Sparse Conv、2D CNN 或 BEV network。