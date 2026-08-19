# PointNet / PointNet++ 为什么重要

## PointNet

点云没有固定顺序，因此需要 permutation-invariant aggregation。

```text
points [N,3]
→ shared MLP per point
→ [N,D]
→ symmetric max pool
→ global feature [D]
```

## 为什么 max pool

无论输入点顺序怎么排列，最大值不变。

## PointNet++

加入 hierarchical neighborhood grouping：局部采样 → PointNet → 更大尺度，类似 CNN 的局部感受野层级。

## 局限

大规模稠密点云中，全点 MLP/邻域搜索成本仍高，后来发展出 sparse conv 和 point transformer。