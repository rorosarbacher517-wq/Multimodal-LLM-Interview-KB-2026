# 16B · Visual Perception 高频面试题

> 先口述，再点对应模块复习。重点不是背模型名，而是把 **输入 → feature/geometry → output → loss/association → deployment** 说清。

## OCR / Document AI

1. OCR detection、recognition、spotting、document parsing 区别？ → [02C](../02C_OCR_Document_AI/README.md)
2. DBNet 为什么用 differentiable binarization？ → [02C](../02C_OCR_Document_AI/02_text_detection_dbnet.md)
3. CTC 为什么不需要字符级对齐？blank 是什么？ → [02C](../02C_OCR_Document_AI/03_crnn_ctc.md)
4. CRNN 和 Transformer OCR 怎么比较？ → [02C](../02C_OCR_Document_AI/04_transformer_ocr.md)
5. Layout analysis 和普通 text detection 差在哪？ → [02C](../02C_OCR_Document_AI/05_layout_reading_order.md)
6. LayoutLMv3 的 text / bbox / image 怎么融合？ → [02C](../02C_OCR_Document_AI/06_layoutlmv3.md)
7. Donut 为什么叫 OCR-free？ → [02C](../02C_OCR_Document_AI/07_donut_ocr_free.md)
8. 表格/公式为什么不能只看字符准确率？ → [02C](../02C_OCR_Document_AI/08_table_formula_chart.md)
9. PaddleOCR-VL-1.6 为什么先 layout 再 VLM recognition？ → [02C](../02C_OCR_Document_AI/11_paddleocr_vl_16.md)
10. MinerU2.5 coarse-to-fine 为什么省计算？ → [02C](../02C_OCR_Document_AI/12_mineru25_pro.md)
11. MinerU2.5-Pro 为什么强调 data engine？ → [02C](../02C_OCR_Document_AI/12_mineru25_pro.md)
12. Document RAG 为什么必须保留 page/bbox/layout？ → [02C](../02C_OCR_Document_AI/15_document_rag.md)

## Pose / Tracking

13. Top-down、bottom-up、one-stage pose 区别？ → [02D](../02D_Pose_Tracking/02_topdown_bottomup.md)
14. Heatmap 和 SimCC 怎么比较？ → [02D](../02D_Pose_Tracking/03_heatmap_regression_simcc.md)
15. ViTPose 为什么强？ → [02D](../02D_Pose_Tracking/04_hrnet_vitpose.md)
16. RTMPose / RTMO / RTMW 分别适合什么？ → [02D](../02D_Pose_Tracking/05_rtmpose_family.md)
17. 2D pose lifting 到 3D 为什么需要时间信息？ → [02D](../02D_Pose_Tracking/06_3d_pose_lifting.md)
18. MOT 的 detector、motion、association 各做什么？ → [02D](../02D_Pose_Tracking/07_mot_pipeline.md)
19. SORT 中 Kalman 和 Hungarian 各做什么？ → [02D](../02D_Pose_Tracking/08_sort_deepsort.md)
20. DeepSORT 为什么要 ReID？ → [02D](../02D_Pose_Tracking/08_sort_deepsort.md)
21. ByteTrack 为什么保留低分 detection？ → [02D](../02D_Pose_Tracking/09_bytetrack.md)
22. BoT-SORT 为什么要 camera motion compensation？ → [02D](../02D_Pose_Tracking/10_botsort_ocsort.md)
23. OC-SORT 的 observation-centric 是什么意思？ → [02D](../02D_Pose_Tracking/10_botsort_ocsort.md)
24. MOTA / IDF1 / HOTA 区别？ → [02D](../02D_Pose_Tracking/11_tracking_metrics.md)
25. Object tracking、point tracking、optical flow 区别？ → [02D](../02D_Pose_Tracking/12_object_point_flow.md)
26. CoTracker 输入输出 shape 是什么？ → [02D](../02D_Pose_Tracking/13_cotracker3.md)
27. SAM2 tracking 和 ByteTrack 怎么选？ → [02D](../02D_Pose_Tracking/14_sam2_tracking.md)

## Depth / 3D Perception

28. Relative depth 和 metric depth 区别？ → [02E](../02E_Depth_3D_Perception/01_depth_types.md)
29. 为什么单目深度有 scale ambiguity？ → [02E](../02E_Depth_3D_Perception/02_monocular_depth_ambiguity.md)
30. Depth Anything V2 的 encoder/decoder 怎么理解？ → [02E](../02E_Depth_3D_Perception/04_depth_anything_v2.md)
31. Video Depth 为什么不能逐帧直接估？ → [02E](../02E_Depth_3D_Perception/05_video_prompt_depth_anything.md)
32. `Z=fB/d` 怎么推？远处为什么误差大？ → [02E](../02E_Depth_3D_Perception/07_stereo_depth.md)
33. Intrinsics、extrinsics、unprojection 分别是什么？ → [02E](../02E_Depth_3D_Perception/06_camera_geometry.md)
34. SfM 和 Bundle Adjustment 分别做什么？ → [02E](../02E_Depth_3D_Perception/08_sfm_bundle_adjustment.md)
35. Point / voxel / pillar / range view 怎么选？ → [02E](../02E_Depth_3D_Perception/09_point_cloud_representations.md)
36. PointNet 为什么对点顺序不敏感？ → [02E](../02E_Depth_3D_Perception/10_pointnet.md)
37. Sparse Conv 和 Point Transformer 怎么比较？ → [02E](../02E_Depth_3D_Perception/11_sparseconv_ptv3.md)
38. PointPillars / SECOND / CenterPoint 区别？ → [02E](../02E_Depth_3D_Perception/13_3d_detection.md)
39. 为什么自动驾驶喜欢 BEV？ → [02E](../02E_Depth_3D_Perception/14_bev_perception.md)
40. Occupancy 比 3D box 多表达了什么？ → [02E](../02E_Depth_3D_Perception/15_occupancy.md)
41. DUSt3R 为什么能弱化传统 feature matching + triangulation？ → [02E](../02E_Depth_3D_Perception/16_dust3r.md)
42. MASt3R 相比 DUSt3R 多了什么？ → [02E](../02E_Depth_3D_Perception/17_mast3r.md)
43. VGGT 一次 forward 输出哪些 3D quantities？ → [02E](../02E_Depth_3D_Perception/18_vggt.md)
44. VGGT-Ω 的 registers / register attention 为什么省内存？ → [02E](../02E_Depth_3D_Perception/19_vggt_omega.md)
45. 3D perception 怎么接 MLLM / VLA？ → [02E](../02E_Depth_3D_Perception/20_3d_to_mllm_vla.md)

## 闭卷通过标准

- 2 分钟解释 PaddleOCR-VL / ByteTrack / Depth Anything / DUSt3R / VGGT 任意一个；
- 能写出 CTC、Kalman+Hungarian、`Z=fB/d`、unprojection 的基本逻辑；
- 能画出 `PDF → layout → OCR/VLM → Markdown → RAG`；
- 能画出 `video → detector → tracker → track_id`；
- 能画出 `multi-view → depth/point map/camera → 3D scene → VLA`。
