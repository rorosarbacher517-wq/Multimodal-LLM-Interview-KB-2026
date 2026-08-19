# Anchor-based 和 Anchor-free 有什么区别？

## 面试一句话

Anchor-based 先定义先验框；Anchor-free 直接以 feature-map 位置为参考预测 box 或边界距离，减少 anchor 的尺度/宽高比设计。

## 核心回答

- Anchor-based 需要预设 anchor sizes / aspect ratios，再判断哪些 anchor 与 GT 匹配。
- Anchor-free 不等于“没有候选位置”；仍然会在 feature-map 网格位置上产生预测。
- YOLOv8、YOLO11 使用 anchor-free detection head。
- Anchor-free 的主要价值是简化设计和 assignment，并不是天然一定更准。
- 对小目标仍然高度依赖 feature resolution、label assignment 和多尺度融合。

## Primary source

- https://docs.ultralytics.com/models/yolov8
