# 02D · Pose / Tracking

> 这一模块连接静态视觉和视频理解：**关键点 → 姿态 → object tracking → point tracking → video memory → MLLM/VLA**。

## 推荐学习顺序

**Pose basics → top-down/bottom-up → ViTPose/RTMPose → 3D pose → SORT/ByteTrack → CoTracker → SAM2 tracking → VLA**

## 问题目录

1. [2D Pose、3D Pose、Mesh Recovery 区别](./01_pose_tasks.md)
2. [Top-down / Bottom-up / One-stage Pose](./02_topdown_bottomup.md)
3. [Heatmap、Regression、SimCC 怎么预测关键点](./03_heatmap_regression_simcc.md)
4. [HRNet / ViTPose：为什么能做强 Pose Backbone](./04_hrnet_vitpose.md)
5. [RTMPose / RTMO / RTMW：实时姿态估计](./05_rtmpose_family.md)
6. [2D → 3D Pose Lifting 与 MotionBERT](./06_3d_pose_lifting.md)
7. [MOT 的完整 Pipeline](./07_mot_pipeline.md)
8. [SORT / DeepSORT：Kalman + Association](./08_sort_deepsort.md)
9. [ByteTrack：为什么低分框也要用](./09_bytetrack.md)
10. [BoT-SORT / OC-SORT：遮挡和相机运动怎么处理](./10_botsort_ocsort.md)
11. [MOTA / IDF1 / HOTA：Tracking 怎么评测](./11_tracking_metrics.md)
12. [Object Tracking、Point Tracking、Optical Flow 区别](./12_object_point_flow.md)
13. [CoTracker3：Track Any Point](./13_cotracker3.md)
14. [SAM2 / Grounded SAM2 如何做 Video Object Tracking](./14_sam2_tracking.md)
15. [Pose / Tracking 为什么对 MLLM 和 VLA 重要](./15_pose_tracking_mllm_vla.md)
16. [Tracking 工程化：Detector、Tracker、Latency 怎么配](./16_tracking_deployment.md)

## 维度速记

```text
2D pose:
image/person crop → K keypoints → [K,2] + confidence

MOT:
frame t detections [Nt,4]
+ previous tracks [M,...]
→ association
→ track_id + box

CoTracker:
video [B,T,3,H,W] + N query points
→ tracks [B,T,N,2]
→ visibility [B,T,N,1]
```

## Primary sources

- MMPose: https://github.com/open-mmlab/mmpose
- ViTPose: https://arxiv.org/abs/2204.12484
- RTMPose: https://arxiv.org/abs/2303.07399
- ByteTrack: https://github.com/FoundationVision/ByteTrack
- BoT-SORT: https://github.com/NirAharon/BoT-SORT
- OC-SORT: https://github.com/noahcao/OC_SORT
- CoTracker3: https://github.com/facebookresearch/co-tracker
