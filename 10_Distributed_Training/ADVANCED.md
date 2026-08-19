# 10 Advanced · Distributed Training Details

### Q1. Context Parallel 和 Sequence Parallel 区别？
术语因框架略有差异。通常 SP 主要分散 layernorm/dropout 等 activation 计算；CP 更直接把长 sequence/context 切到多卡并处理 attention 通信。

### Q2. 为什么 Long Context 特别需要 Context Parallel？
单卡 activation 和 attention/KV 随 sequence 变大，即使参数能放下，context 本身也可能放不下。

### Q3. GPipe Schedule 的问题？
先 forward 多个 microbatches 再 backward，会产生 pipeline bubble 和较高 activation memory。

### Q4. 1F1B 是什么？
Pipeline warmup 后尽量交替 one-forward-one-backward，降低 peak activation 和 bubble。

### Q5. Interleaved Pipeline 有什么意义？
每张设备持有多个 virtual stages，让 pipeline 更细、降低 bubble，但调度和通信更复杂。

### Q6. Communication Overlap 是什么？
把 all-gather/reduce-scatter/all-reduce 与独立计算并行，隐藏一部分通信 latency。

### Q7. 为什么 TP 更偏节点内？
TP 每层频繁 collective，对 latency/bandwidth 很敏感，因此常优先放在 NVLink/NVSwitch 域内。

### Q8. 为什么 DP 更适合跨节点？
DP 通常每个 step 做梯度/参数相关 collective，通信频率相对 layer-wise TP 低，更容易跨较慢网络扩展。

### Q9. EP 的 All-to-All 为什么难？
每个 token 根据 router 发到不同 expert GPU，通信 pattern 不规则，还受 expert imbalance 影响。

### Q10. CPU / NVMe Offload 是什么？
把 optimizer/parameter state 部分放 CPU 或 NVMe，进一步省 GPU memory，但受 PCIe/NVMe bandwidth 限制。

### Q11. Sharded Checkpoint 为什么要 Reshard？
训练 world size 与恢复/推理 world size 可能不同，需要把旧 shard 重组为新的分片布局。

### Q12. Straggler 是什么？
一个 rank 比其他 rank 慢，collective 时所有卡都等它。多模态 variable-length batch 很容易产生 straggler。

### Q13. 如何减轻多模态 Straggler？
按 estimated FLOPs/visual tokens bucket；动态 batch；限制极端长样本；更平衡地分配视频/多图数据。

### Q14. MFU 是什么？
Model FLOPs Utilization：实际有用模型 FLOPs 相对硬件理论/可达峰值的比例，用于判断训练算力利用率。

### Q15. 大规模训练拓扑设计的回答框架？
**模型结构 → memory estimate → intra-node TP/EP → inter-node DP/PP/CP → communication volume → overlap → checkpoint/failure recovery。**
