# SLAM / VIO 在做什么？

SLAM 同时估计相机/机器人轨迹和环境地图：
```text
observations → pose_t + map
```

典型视觉 SLAM 包含 feature/front-end、data association、pose optimization、loop closure。

VIO 进一步融合 IMU，加速度/角速度能提供高频运动约束，视觉负责抑制漂移。

## 和 SfM 区别
SfM 更偏离线多图重建；SLAM 更强调在线定位与持续建图。
