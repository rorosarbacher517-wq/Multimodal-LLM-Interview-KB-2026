# MOT 的完整 Pipeline

## 面试一句话

Multi-Object Tracking 的核心不是“每帧检测”，而是给同一个对象在不同帧维持稳定的 `track_id`。

## Tracking-by-Detection

```text
Frame t
→ Detector
→ boxes + scores + classes
→ Motion prediction
→ Similarity / IoU / appearance
→ Data association
→ matched / new / lost tracks
→ track_id
```

## 三个核心问题

1. detector 漏检；
2. 遮挡后重新出现；
3. 多个相似对象交叉导致 ID switch。

## 工程上

Detector 通常决定大部分计算量；tracker 本身可以很轻。