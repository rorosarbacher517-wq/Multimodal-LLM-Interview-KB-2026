# Heatmap、Regression、SimCC 怎么预测关键点

## Heatmap

每个关键点输出一张概率图：`[B,K,Hh,Wh]`，取峰值得到坐标。

优点：空间监督稳定；缺点：高分辨率 heatmap 占显存，量化误差存在。

## Direct Regression

直接预测 `[B,K,2]`。

优点：简单；缺点：学习空间分布更难。

## SimCC

把 x/y 坐标分别做 1-D classification：

```text
x logits [B,K,Lx]
y logits [B,K,Ly]
```

兼顾分类监督稳定性和较低的二维 heatmap 成本。

## 面试结论

关键是理解：Pose head 在做的是 **从视觉 feature 到空间坐标概率分布**。