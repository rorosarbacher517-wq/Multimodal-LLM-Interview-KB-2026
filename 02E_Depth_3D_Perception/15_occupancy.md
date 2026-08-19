# 3D Occupancy 为什么比 Box 更完整

## Box 的局限

3D box 只描述预定义 object classes，无法完整表示墙、路沿、植被、未知障碍物和自由空间。

## Occupancy

把 3D 空间划成 voxel，每个 voxel 预测：

- occupied / free；
- semantic class；
- 有时还预测 flow/motion。

## Pipeline

```text
camera/LiDAR
→ 3D/BEV features
→ occupancy grid [X,Y,Z,C]
```

## 代价

3D grid 很大，需要 sparse representation、multi-scale 或压缩。

## 与 world model 关系

occupancy 更接近“世界状态”，因此比 boxes 更适合作为 planning 和 future prediction 的中间表示。