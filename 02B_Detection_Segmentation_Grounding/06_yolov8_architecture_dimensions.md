# YOLOv8 的底层结构和维度怎么变化？

## 面试一句话

YOLOv8 可以记成：**Conv/C2f Backbone → SPPF → PAN-FPN Neck → P3/P4/P5 Anchor-free Decoupled Head**。

## 结构

- Backbone 使用 stride=2 Conv 持续降采样，核心重复块是 **C2f**。
- **SPPF** 在深层扩大有效感受野。
- Neck 通过 Upsample + Concat 融合 P3/P4/P5。
- Detect head 是 anchor-free、decoupled。
- 官方 YOLOv8 detection head 使用 DFL（`reg_max=16`）进行边界分布回归。

## 维度

```text
[B,3,640,640]
   ↓ /2
320×320
   ↓ /2
160×160
   ↓ /2
P3 = 80×80
   ↓ /2
P4 = 40×40
   ↓ /2
P5 = 20×20

80² + 40² + 20² = 8400 spatial locations
```

通道数取决于 n/s/m/l/x 的 width scaling，不建议死背。

## Primary sources

- https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/models/v8/yolov8.yaml
- https://github.com/ultralytics/ultralytics/blob/main/docs/en/guides/yolo-architecture.md
