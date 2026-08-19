# Semantic / Instance / Panoptic Segmentation 区别

## 面试一句话
- **Semantic**：每个像素是什么类别，不区分同类实例。
- **Instance**：每个目标实例单独一个 mask。
- **Panoptic**：把 stuff（天空、路面）和 things（人、车实例）统一到完整像素级解析。

## 输出形态
```text
Semantic: [H,W] class id
Instance: {mask_i, class_i, score_i}
Panoptic: [H,W] segment id + segment metadata
```

## 常见追问
**为什么 detection 不能替代 segmentation？**
Box 只给粗区域，无法表达精确边界、孔洞、细长结构和像素级占用。
