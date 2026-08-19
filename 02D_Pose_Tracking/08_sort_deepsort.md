# SORT / DeepSORT：Kalman + Association

## SORT

```text
previous track
→ Kalman predict
→ detector boxes
→ IoU cost matrix
→ Hungarian matching
→ Kalman update
```

## DeepSORT

在 motion/IoU 之外加入 appearance embedding（ReID），减少遮挡后 ID switch。

## Kalman Filter 做什么

根据历史状态预测下一帧位置，并在 detector 给出 observation 后更新状态估计。

## Hungarian 做什么

在一组 tracks 和 detections 之间求全局最小匹配成本。

## 易错点

SORT/DeepSORT 本身不负责目标检测。