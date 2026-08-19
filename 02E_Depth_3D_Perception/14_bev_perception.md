# BEVFormer / BEVFusion：为什么转到 Bird's-Eye View

## 面试一句话

BEV 把多相机/LiDAR 的信息统一到俯视坐标系，便于直接做道路、车辆、轨迹和规划。

## Camera → BEV

```text
multi-camera images
→ image features
→ geometry / attention lifting
→ BEV grid [Hbev,Wbev,C]
→ 3D detection / map / occupancy
```

## BEVFormer

用 spatial cross-attention 从多相机 feature 采样到 BEV queries，并用 temporal attention 利用历史 BEV。

## BEVFusion

把 camera 和 LiDAR 特征映射到统一 BEV，再融合。

## 为什么适合自动驾驶

规划本来就在地面/世界坐标中进行，BEV 比每个 camera view 更接近下游表示。