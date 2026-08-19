# 02E · Depth / 3D Perception

> 这一模块补齐从二维图像到三维世界建模的基础：**depth → camera geometry → point cloud → 3D detection / BEV → multi-view reconstruction → 3D foundation models → VLA**。

## 推荐学习顺序

**Depth basics → camera geometry → stereo/SfM → point cloud → 3D detection/BEV → DUSt3R/MASt3R → VGGT/VGGT-Ω → MLLM/VLA**

## 问题目录

1. [Relative Depth、Metric Depth、Disparity 区别](./01_depth_types.md)
2. [单目深度为什么是病态问题](./02_monocular_depth_ambiguity.md)
3. [DPT / MiDaS：Transformer Depth 基础](./03_dpt_midas.md)
4. [Depth Anything V2：Foundation Depth](./04_depth_anything_v2.md)
5. [Video Depth Anything / Prompt Depth Anything](./05_video_prompt_depth_anything.md)
6. [Camera Intrinsics / Extrinsics / Projection](./06_camera_geometry.md)
7. [Stereo：Disparity 如何变成 Depth](./07_stereo_depth.md)
8. [SfM / Bundle Adjustment 在做什么](./08_sfm_bundle_adjustment.md)
9. [Point Cloud：Point / Voxel / Pillar / Range View](./09_point_cloud_representations.md)
10. [PointNet / PointNet++ 为什么重要](./10_pointnet.md)
11. [Sparse Conv / Point Transformer v3](./11_sparseconv_ptv3.md)
12. [2025–2026 Point Cloud Foundation：Sonata / Concerto / Utonia](./12_pointcloud_foundation_2026.md)
13. [3D Detection：PointPillars / SECOND / CenterPoint](./13_3d_detection.md)
14. [BEVFormer / BEVFusion：为什么转到 Bird's-Eye View](./14_bev_perception.md)
15. [3D Occupancy 为什么比 Box 更完整](./15_occupancy.md)
16. [DUSt3R：为什么可以弱化传统 SfM Pipeline](./16_dust3r.md)
17. [MASt3R：3D Matching 与 Scalable Alignment](./17_mast3r.md)
18. [VGGT：Feed-forward 3D Geometry Foundation](./18_vggt.md)
19. [VGGT-Ω：2026 的动态场景与高效 3D Foundation](./19_vggt_omega.md)
20. [3D Perception 如何接 MLLM / VLA / World Model](./20_3d_to_mllm_vla.md)

## 一张图理解 3D Perception

```text
Image / Multi-view / Video / LiDAR
            ↓
2D features / depth / correspondences
            ↓
Camera geometry / unprojection
            ↓
Point cloud / point map / BEV / occupancy
            ↓
3D objects + camera pose + scene geometry
            ↓
Spatial reasoning / planning / action
```

## 2026 特别值得掌握

- Depth Anything V2 + Video/Prompt Depth Anything；
- DUSt3R / MASt3R 把 matching + reconstruction 变成 learned point-map prediction；
- VGGT 直接预测 camera、depth、point maps、3D tracks；
- VGGT-Ω 进一步扩展动态场景并降低训练内存；
- Pointcept 2025–2026 的 Sonata / Concerto / Utonia 体现点云 foundation encoder 路线。

## Primary sources

- Depth Anything V2: https://github.com/DepthAnything/Depth-Anything-V2
- DUSt3R: https://github.com/naver/dust3r
- MASt3R: https://github.com/naver/mast3r
- VGGT: https://github.com/facebookresearch/vggt
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- Pointcept: https://github.com/Pointcept/Pointcept
