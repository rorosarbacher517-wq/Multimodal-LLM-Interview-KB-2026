# YOLO11 相比 YOLOv8 结构上改了什么？

## 面试一句话

YOLO11 仍然是 P3/P4/P5 多尺度 YOLO，但核心 block 从 C2f 演化为 **C3k2**，高层加入 **C2PSA**，继续使用 anchor-free decoupled detection head。

## 官方 YAML 主链

```text
Conv
 → C3k2
 → downsample
 → C3k2
 → ...
 → SPPF
 → C2PSA
 → Upsample + Concat
 → C3k2
 → Detect(P3,P4,P5)
```

## 维度

对 640×640 输入：

```text
P3/8  = 80×80
P4/16 = 40×40
P5/32 = 20×20
```

YOLO11 detection head 仍使用 DFL。YOLO11 没有正式论文，具体架构应以 Ultralytics 官方 YAML/docs 为准。

## Primary sources

- https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/models/11/yolo11.yaml
- https://docs.ultralytics.com/models/yolo11
