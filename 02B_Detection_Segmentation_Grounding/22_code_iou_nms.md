# 手写 IoU / NMS：面试代码题

## IoU

```python
def iou(box1, box2):
    # box = [x1, y1, x2, y2]
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    inter = max(0, x2-x1) * max(0, y2-y1)
    a1 = max(0, box1[2]-box1[0]) * max(0, box1[3]-box1[1])
    a2 = max(0, box2[2]-box2[0]) * max(0, box2[3]-box2[1])
    return inter / (a1 + a2 - inter + 1e-9)
```

## NMS 思路

```text
按 score 从高到低排序
→ 取最高分框 keep
→ 删除与 keep 的 IoU > threshold 的框
→ 对剩余框重复
```

```python
def nms(boxes, scores, thr=0.5):
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    keep = []
    while order:
        i = order.pop(0)
        keep.append(i)
        order = [j for j in order if iou(boxes[i], boxes[j]) <= thr]
    return keep
```

## 面试追问

- 为什么 Soft-NMS 不直接删除？
- class-aware / class-agnostic NMS 区别？
- 为什么 DETR / YOLOv10 / YOLO26 可以 NMS-free？
- 真实工程中应使用 vectorized / CUDA 实现，不要用上面的 Python 循环版做线上推理。
