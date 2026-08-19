# 10 · Distributed Training

## Q1. 为什么单卡训不了大模型？

显存不仅放参数，还要放：

- gradients；
- optimizer states；
- activations；
- temporary buffers；
- 多模态视觉特征。

Adam 混合精度训练的状态常比“模型权重大小”大很多。

## Q2. 一个参数训练时大概占多少显存？

粗略思路（具体实现会变）：

- FP16/BF16 weight：2 bytes；
- grad：约 2 bytes；
- Adam m/v：常各 4 bytes；
- 可能还有 FP32 master weight：4 bytes。

因此经常用 **12–16 bytes/parameter** 做粗预算，再加 activation。

## Q3. DDP 怎么工作？

每张 GPU：

- 有完整模型；
- 处理不同 mini-batch；
- backward 后对 gradient 做 all-reduce；
- 每张卡执行相同 optimizer update。

优点简单高效，缺点模型必须单卡能放下。

## Q4. Data Parallel 为什么不能解决模型太大的问题？

因为每张卡仍保存完整参数/optimizer states。它只是切 batch，不切模型。

模型本身放不下时需要 FSDP/ZeRO/TP/PP 等 model sharding。

## Q5. ZeRO 三个 stage 怎么记？

- Stage 1：切 optimizer states；
- Stage 2：再切 gradients；
- Stage 3：再切 parameters。

越往后越省显存，但通信和实现复杂度更高。

## Q6. FSDP 的核心是什么？

Fully Sharded Data Parallel 把参数、梯度、optimizer state 分片。需要某层计算时再 all-gather 参数，计算后重新 shard/release。

效果：每张卡不必长期保存整个模型。

## Q7. FSDP2 相比传统 FSDP1 为什么值得掌握？

PyTorch FSDP2 的 `fully_shard` 基于 DTensor/per-parameter sharding，组合性更好，也更贴近新 PyTorch distributed stack。

面试重点不是 API 名，而是理解：

**参数平时分片 → 计算前 all-gather → backward 后 reduce-scatter → 再分片。**

官方：[PyTorch fully_shard](https://docs.pytorch.org/docs/main/distributed.fsdp.fully_shard.html)

## Q8. Tensor Parallelism 切什么？

把单个大矩阵乘拆到多 GPU，例如按列/行切 Linear：

```text
Y = XW
W = [W1, W2, ...]
```

每卡只算部分输出/部分 reduction。

适合单层本身很大，但每层都会产生 collective communication。

## Q9. Pipeline Parallelism 切什么？

把不同层放不同 GPU stage：

```text
GPU0: layers 0-9
GPU1: 10-19
GPU2: 20-29
```

需要 micro-batch pipeline 减少 bubble。

## Q10. Expert Parallelism 为什么是 MoE 特有重点？

不同 experts 分到不同 GPU。router 决定 token 要发送到哪张卡，形成 all-to-all communication。

瓶颈：

- expert imbalance；
- 网络带宽；
- token dispatch/gather；
- capacity overflow。

## Q11. TP、PP、DP、EP 怎么组合？

大模型常采用多维并行：

```text
world_size = DP × TP × PP × EP
```

不是维度越多越好。选择取决于：

- 模型是否 MoE；
- 单层大小；
- 节点内 NVLink / 节点间网络；
- batch；
- sequence length。

## Q12. Sequence Parallelism 是什么？

把 sequence/token 维上的 activation 或某些计算分散到不同 GPU，常与 TP 配合减少 activation memory 和重复计算。

长 context、视频 token 多时更有价值。

## Q13. Activation Checkpointing 如何省显存？

forward 不保存所有中间 activation，backward 时重新计算。

交换：

**更少显存 ↔ 更多计算。**

常对 Transformer block 做 checkpoint。

## Q14. Gradient Accumulation 有什么作用？

小 micro-batch 多次 backward 累积梯度，再 optimizer step：

```text
effective batch
= micro_batch × accumulation_steps × data_parallel_size
```

它解决 batch 显存，不解决单个样本/单模型本身放不下。

## Q15. 多模态训练为什么容易 load imbalance？

不同样本：

- 图片数不同；
- 分辨率不同；
- 视频帧数不同。

同一个 batch 里 FLOPs 差异巨大，导致某些 rank 慢很多。应做 token-based bucketing、dynamic batching、packing。

## Q16. All-Reduce、All-Gather、Reduce-Scatter 区别？

- All-Reduce：每卡拿到 reduction 后完整结果；
- All-Gather：每卡收集所有 shard；
- Reduce-Scatter：先 reduce，再把结果 shard 给不同卡。

DDP 常见 all-reduce；FSDP 常见 all-gather + reduce-scatter。

## Q17. 分布式训练 checkpoint 为什么难？

sharded 模型可能每卡只拥有一部分 state。需要：

- distributed checkpoint；
- metadata；
- world-size compatible reshard；
- optimizer state；
- RNG/data-loader state；
- 原子写入和失败恢复。

真正的大规模训练必须支持 preemption/resume。

## Q18. 大模型训练性能排查顺序？

1. GPU utilization；
2. data loader / CPU；
3. kernel efficiency；
4. communication overlap；
5. imbalance；
6. activation recompute；
7. I/O/checkpoint；
8. NCCL/network。

先 profiling，再改 parallel strategy；不要看到“慢”就直接加 GPU。