# 02E · Depth / 3D Perception / Geometry

> 从二维图像进入三维世界：**Depth → Camera Geometry → SfM/SLAM → Point Cloud/BEV → NeRF/3DGS → Feed-forward 3D Foundation → VLA/World Model**。

## 问题目录
1. [Relative Depth / Metric Depth / Disparity](./01_depth_types.md)
2. [Monocular Depth Ambiguity](./02_monocular_depth_ambiguity.md)
3. [DPT / MiDaS](./03_dpt_midas.md)
4. [Depth Anything V2](./04_depth_anything_v2.md)
5. [Video / Prompt Depth Anything](./05_video_prompt_depth_anything.md)
6. [Camera Intrinsics / Extrinsics / Projection](./06_camera_geometry.md)
7. [Stereo: Disparity → Depth](./07_stereo_depth.md)
8. [SfM / Bundle Adjustment](./08_sfm_bundle_adjustment.md)
9. [Point / Voxel / Pillar / Range View](./09_point_cloud_representations.md)
10. [PointNet / PointNet++](./10_pointnet.md)
11. [Sparse Conv / Point Transformer v3](./11_sparseconv_ptv3.md)
12. [Point-cloud Foundation Models](./12_pointcloud_foundation_2026.md)
13. [PointPillars / SECOND / CenterPoint](./13_3d_detection.md)
14. [BEVFormer / BEVFusion](./14_bev_perception.md)
15. [3D Occupancy](./15_occupancy.md)
16. [DUSt3R](./16_dust3r.md)
17. [MASt3R](./17_mast3r.md)
18. [VGGT](./18_vggt.md)
19. [VGGT-Ω](./19_vggt_omega.md)
20. [3D → MLLM / VLA / World Model](./20_3d_to_mllm_vla.md)
21. [SLAM / VIO](./21_slam_vio.md)
22. [NeRF](./22_nerf.md)
23. [3D Gaussian Splatting](./23_3d_gaussian_splatting.md)
24. [Camera/LiDAR/IMU Calibration & Fusion](./24_sensor_calibration_fusion.md)

## 一张图
```text
Image / Multi-view / Video / LiDAR / IMU
            ↓
depth / features / correspondences / motion
            ↓
Camera Geometry / Calibration / SfM / SLAM
            ↓
Point Cloud / BEV / Occupancy / Scene Representation
            ↓
Detection / Reconstruction / Rendering / Tracking
            ↓
Spatial Reasoning / Planning / Action
```

## Primary sources
- Depth Anything V2: https://github.com/DepthAnything/Depth-Anything-V2
- PointNet: https://arxiv.org/abs/1612.00593
- BEVFormer: https://arxiv.org/abs/2203.17270
- BEVFusion: https://arxiv.org/abs/2205.13542
- NeRF: https://arxiv.org/abs/2003.08934
- 3D Gaussian Splatting: https://arxiv.org/abs/2308.04079
- DUSt3R: https://arxiv.org/abs/2312.14132
- MASt3R: https://arxiv.org/abs/2406.09756
- VGGT: https://arxiv.org/abs/2503.11651
