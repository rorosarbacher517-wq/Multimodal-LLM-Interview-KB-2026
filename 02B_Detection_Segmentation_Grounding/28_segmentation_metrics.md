# Segmentation Metrics：IoU / mIoU / Dice / Mask AP

## IoU
```text
IoU = intersection / union
```

## mIoU
对各 semantic classes 的 IoU 求平均。

## Dice
更强调 overlap，和 F1 形式相近。

## Mask AP
Instance segmentation 常按不同 mask IoU thresholds 统计 AP。

## 易错点
Semantic mIoU 和 COCO-style instance Mask AP 不是同一种评测，不能直接比较。
