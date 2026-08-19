# Segmentation Loss：CE / BCE / Dice / Focal

## Cross Entropy / BCE
逐像素分类；multi-class 常用 CE，binary/multi-label mask 常用 BCE。

## Dice Loss
关注预测 mask 与 GT 的重叠：
```text
Dice = 2|P∩G| / (|P|+|G|)
```
对前景像素很少的类别特别有用。

## Focal Loss
降低大量 easy negatives 的权重，让训练更关注 hard examples。

## 实际
常组合 BCE/CE + Dice，而不是认为一种 loss 对所有 segmentation 都最好。
