# 04_FlashAttention到底优化什么

## 面试一句话

FlashAttention 不改变注意力数学结果，核心是减少 HBM↔SRAM 数据搬运，并用 tiling 提高硬件利用率。

## 核心回答

- 标准 attention 的瓶颈不只是 FLOPs，还包括 IO。
- FlashAttention-3 针对 Hopper 异步流水和 FP8。
- FlashAttention-4 面向 Blackwell，重新设计 pipeline/softmax/内存访问。
- 它不会把理论 O(N²) 直接变成 O(N)。
## 易错点

- 不要把 FlashAttention 说成稀疏注意力。

## 参考

- https://arxiv.org/abs/2407.08608
- https://arxiv.org/abs/2603.05451
