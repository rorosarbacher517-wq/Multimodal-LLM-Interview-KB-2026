# 02B · Detection / Segmentation / Grounding

> 完整视觉定位链：**Detection → Segmentation → Open-Vocabulary Grounding → Promptable Segmentation → Auto-labeling → MLLM Tool**。

## 推荐顺序
检测基础 → YOLO/DETR → segmentation fundamentals → SAM → GroundingDINO → Grounded SAM → 自动标注/Agent tool

## 问题目录
1. [Detection、Segmentation、Grounding 区别](./01_detection_segmentation_grounding.md)
2. [One-stage、Two-stage、DETR](./02_one_stage_two_stage_detr.md)
3. [Anchor-based vs Anchor-free](./03_anchor_based_vs_anchor_free.md)
4. [FPN / PAN / Multi-scale](./04_fpn_pan_multiscale.md)
5. [NMS、NMS-free、Label Assignment](./05_nms_nmsfree_assignment.md)
6. [YOLOv8 结构与维度](./06_yolov8_architecture_dimensions.md)
7. [YOLOv9：PGI / GELAN](./07_yolov9_pgi_gelan.md)
8. [YOLOv10：End-to-End NMS-free](./08_yolov10_end_to_end.md)
9. [YOLO11 结构与维度](./09_yolo11_architecture_dimensions.md)
10. [YOLOv8/v9/v10/11 对比](./10_yolo8_9_10_11_compare.md)
11. [YOLO26 当前路线](./11_yolo26_latest.md)
12. [YOLO-World / YOLOE / Open Vocabulary](./12_yolo_world_yoloe.md)
13. [DETR / Deformable DETR / DINO](./13_detr_family.md)
14. [RT-DETR](./14_rt_detr.md)
15. [SAM 结构与维度](./15_sam_architecture_dimensions.md)
16. [SAM Prompt Encoder / Data Engine](./16_sam_prompt_and_data_engine.md)
17. [SAM2 Streaming Memory](./17_sam2_video_memory.md)
18. [GroundingDINO：Phrase → Box](./18_groundingdino_architecture.md)
19. [GroundingDINO 1.5 / DINO-X](./19_groundingdino15_dinox.md)
20. [Grounded SAM / Auto Annotation](./20_grounded_sam_auto_annotation.md)
21. [MLLM 为什么仍需要专用 Perception Tools](./21_mllm_perception_tools.md)
22. [手写 IoU / NMS](./22_code_iou_nms.md)
23. [Semantic / Instance / Panoptic Segmentation](./23_semantic_instance_panoptic.md)
24. [U-Net / DeepLab](./24_unet_deeplab.md)
25. [Mask R-CNN](./25_mask_rcnn.md)
26. [Mask2Former](./26_mask2former.md)
27. [Segmentation Losses](./27_segmentation_losses.md)
28. [Segmentation Metrics](./28_segmentation_metrics.md)
29. [Open-Vocabulary Segmentation](./29_open_vocabulary_segmentation.md)
30. [Segmentation Deployment](./30_segmentation_deployment.md)

## 维度速记
```text
YOLO 640 input:
P3/8  = 80×80
P4/16 = 40×40
P5/32 = 20×20

SAM:
1024×1024 → patch16 → 64×64
→ image embedding [B,256,64,64]

GroundingDINO:
image multi-scale features + text tokens
→ language-guided queries
→ boxes + phrase/token alignment
```

## Primary sources
- YOLO docs: https://docs.ultralytics.com/models/
- DETR: https://arxiv.org/abs/2005.12872
- Mask R-CNN: https://arxiv.org/abs/1703.06870
- Mask2Former: https://arxiv.org/abs/2112.01527
- SAM: https://arxiv.org/abs/2304.02643
- SAM2: https://arxiv.org/abs/2408.00714
- GroundingDINO: https://arxiv.org/abs/2303.05499
