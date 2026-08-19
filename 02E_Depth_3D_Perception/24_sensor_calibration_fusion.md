# Camera / LiDAR / IMU Calibration 与 Fusion

多传感器融合第一步不是“把 feature concat”，而是先统一空间和时间坐标。

需要考虑：
- camera intrinsics；
- sensor-to-sensor extrinsics；
- timestamp synchronization；
- distortion；
- ego pose。

```text
LiDAR point (sensor frame)
→ extrinsic transform
→ camera frame
→ intrinsic projection
→ image pixel
```

标定误差会让后续 BEV fusion、3D detection 和 VLA 空间推理系统性偏移。
