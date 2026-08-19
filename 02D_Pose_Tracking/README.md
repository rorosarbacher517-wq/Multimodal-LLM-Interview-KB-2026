# 02D · Pose / Tracking / Motion

> 从静态关键点到视频状态：**Pose → MOT/SOT → Dense Motion → Point Tracking → Video Memory → VLA**。

## 问题目录
1. [2D Pose、3D Pose、Mesh Recovery](./01_pose_tasks.md)
2. [Top-down / Bottom-up / One-stage Pose](./02_topdown_bottomup.md)
3. [Heatmap / Regression / SimCC](./03_heatmap_regression_simcc.md)
4. [HRNet / ViTPose](./04_hrnet_vitpose.md)
5. [RTMPose / RTMO / RTMW](./05_rtmpose_family.md)
6. [2D→3D Pose / MotionBERT](./06_3d_pose_lifting.md)
7. [MOT 完整 Pipeline](./07_mot_pipeline.md)
8. [SORT / DeepSORT](./08_sort_deepsort.md)
9. [ByteTrack](./09_bytetrack.md)
10. [BoT-SORT / OC-SORT](./10_botsort_ocsort.md)
11. [MOTA / IDF1 / HOTA](./11_tracking_metrics.md)
12. [Object Tracking / Point Tracking / Optical Flow](./12_object_point_flow.md)
13. [CoTracker3](./13_cotracker3.md)
14. [SAM2 / Grounded SAM2 Tracking](./14_sam2_tracking.md)
15. [Pose / Tracking → MLLM / VLA](./15_pose_tracking_mllm_vla.md)
16. [Tracking Deployment](./16_tracking_deployment.md)
17. [RAFT / Optical Flow](./17_raft_optical_flow.md)
18. [Single-Object Tracking](./18_single_object_tracking.md)

## 维度速记
```text
Pose: image/person crop → [K,2] + confidence
MOT: detections [Nt,4] + tracks → association → id+box
Optical flow: frames → [B,2,H,W]
CoTracker: video + N query points → [B,T,N,2] + visibility
```

## Primary sources
- MMPose: https://github.com/open-mmlab/mmpose
- ViTPose: https://arxiv.org/abs/2204.12484
- ByteTrack: https://arxiv.org/abs/2110.06864
- RAFT: https://arxiv.org/abs/2003.12039
- CoTracker3: https://arxiv.org/abs/2410.11831
