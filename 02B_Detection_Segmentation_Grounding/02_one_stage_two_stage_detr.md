# One-stage、Two-stage、DETR 三类检测器怎么比较？

## 面试一句话

三者主要区别在候选生成和匹配方式：YOLO 做 dense prediction；Faster R-CNN 先 proposal 再分类回归；DETR 用 object queries 做集合预测。

## 核心回答

- **One-stage**：单次前向完成密集预测，速度快，YOLO 是代表。
- **Two-stage**：RPN 先产生 proposals，再做 RoI 特征、分类和 bbox regression。
- **DETR-style**：固定数量 object queries 与图像特征交互，再通过 Hungarian matching 做一一匹配。
- 工程上不要简单说“YOLO 快、DETR 慢”；RT-DETR 已经把 DETR 路线推到实时，YOLOv10/YOLO26 也在向端到端 NMS-free 靠拢。

## 判断标准

看四件事：**候选从哪里来、监督是 one-to-many 还是 one-to-one、是否依赖 NMS、多尺度特征怎么融合。**
