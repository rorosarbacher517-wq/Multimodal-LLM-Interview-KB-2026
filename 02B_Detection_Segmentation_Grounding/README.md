# 02B · Detection / Segmentation / Grounding

> 这一模块补齐多模态算法岗常见的视觉感知底座：**YOLO / DETR / RT-DETR / SAM / SAM 2 / GroundingDINO / Grounded SAM / YOLOE**。
>
> 学习目标不是背模型名，而是能说明：**输入 → backbone/queries → multi-scale features → boxes/masks → loss/matching → deployment → 与 MLLM 的关系**。

## 推荐学习顺序

**检测基础 → YOLO → DETR → SAM → GroundingDINO → Grounded SAM → 自动标注 / MLLM Tool**

## 问题目录

1. [Detection、Segmentation、Grounding 区别](./01_detection_segmentation_grounding.md)
2. [One-stage、Two-stage、DETR 三类检测器](./02_one_stage_two_stage_detr.md)
3. [Anchor-based vs Anchor-free](./03_anchor_based_vs_anchor_free.md)
4. [FPN / PAN / Multi-scale 为什么重要](./04_fpn_pan_multiscale.md)
5. [NMS、NMS-free 与 Label Assignment](./05_nms_nmsfree_assignment.md)
6. [YOLOv8 底层结构与维度](./06_yolov8_architecture_dimensions.md)
7. [YOLOv9：PGI 与 GELAN](./07_yolov9_pgi_gelan.md)
8. [YOLOv10：端到端 NMS-free](./08_yolov10_end_to_end.md)
9. [YOLO11 底层结构与维度](./09_yolo11_architecture_dimensions.md)
10. [YOLOv8 / v9 / v10 / 11 怎么比较](./10_yolo8_9_10_11_compare.md)
11. [YOLO26：截至 2026 的 Ultralytics 新路线](./11_yolo26_latest.md)
12. [YOLO-World / YOLOE / Open-Vocabulary Detection](./12_yolo_world_yoloe.md)
13. [DETR / Hungarian Matching / Deformable DETR / DINO](./13_detr_family.md)
14. [RT-DETR 为什么能实时](./14_rt_detr.md)
15. [SAM 底层结构与维度](./15_sam_architecture_dimensions.md)
16. [SAM 的 Prompt Encoder 与 Data Engine](./16_sam_prompt_and_data_engine.md)
17. [SAM 2 / SAM 2.1：Streaming Memory](./17_sam2_video_memory.md)
18. [GroundingDINO 底层结构与 Phrase → Box](./18_groundingdino_architecture.md)
19. [GroundingDINO 1.5 / DINO-X](./19_groundingdino15_dinox.md)
20. [Grounded SAM / Grounded SAM 2 / 自动标注](./20_grounded_sam_auto_annotation.md)
21. [MLLM 为什么还需要 YOLO / SAM / GroundingDINO](./21_mllm_perception_tools.md)
22. [手写 IoU / NMS：面试代码题](./22_code_iou_nms.md)

## 维度速记

```text
YOLO (640 input)
P3/8  = 80×80
P4/16 = 40×40
P5/32 = 20×20

SAM
1024×1024 → patch16 → 64×64 grid
→ image embedding [B,256,64,64]

GroundingDINO
image features + text tokens
→ language-guided queries
→ boxes + phrase/token alignment

Grounded SAM
text → GroundingDINO box → SAM/SAM2 mask
```

## Primary sources

- YOLOv8: https://docs.ultralytics.com/models/yolov8
- YOLOv9: https://arxiv.org/abs/2402.13616
- YOLOv10: https://arxiv.org/abs/2405.14458
- YOLO11: https://docs.ultralytics.com/models/yolo11
- YOLO26: https://docs.ultralytics.com/models/yolo26
- RT-DETR: https://arxiv.org/abs/2304.08069
- SAM: https://arxiv.org/abs/2304.02643
- SAM 2: https://arxiv.org/abs/2408.00714
- GroundingDINO: https://arxiv.org/abs/2303.05499
- Grounded SAM: https://arxiv.org/abs/2401.14159
- DINO-X: https://arxiv.org/abs/2411.14347
