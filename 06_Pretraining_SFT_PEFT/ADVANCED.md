# 06 Advanced · Scaling, Packing, Long Context & Reproducible Training

### Q1. Training Token Budget 为什么比“样本数”更重要？
文本长度、视觉 token、视频帧数差异巨大。真正决定 compute 的常常是 total tokens / FLOPs，而不是 samples。

### Q2. Scaling Law 给工程什么启示？
模型参数、数据量和 compute 要匹配。只增模型不增有效数据，或数据远大于模型可吸收能力，都可能浪费预算。

### Q3. Sequence Packing 是什么？
把多个短样本拼到一个长 sequence 减少 padding：
```text
sample A | sample B | sample C
```
需要正确 attention boundary 和 loss mask，避免样本之间互相看见不该看的内容。

### Q4. Packing 和 Padding 的 trade-off？
Packing 提升 token utilization，但 collator/mask 更复杂；variable-resolution multimodal packing 还要处理视觉 placeholder 与 feature offset。

### Q5. Token-based Dynamic Batch 怎么做？
固定每 batch 最大 token budget：短样本可多放，长样本少放，从而稳定显存和 step time。

### Q6. Long-context Training 为什么不能只改 Position Limit？
模型需要真正见过长距离依赖，并解决 RoPE scaling、activation/KV、数据分布和 optimizer stability。

### Q7. Long-context 数据如何构造？
- long documents/interleaved data；
- multi-document retrieval tasks；
- long video；
- synthetic long-range dependency。

要避免只是把无关短样本机械 concat。

### Q8. Visual Token Curriculum 有什么意义？
早期可用较低 resolution/token 提高吞吐，后期逐步提高高分辨率/多图比例；是否有效需 controlled ablation。

### Q9. Gradient Accumulation 改变了什么？
增加 effective batch，不降低单样本 activation；还会改变 optimizer update frequency，需要同步考虑 scheduler。

### Q10. Global Batch Size 变大后 Learning Rate 一定线性变大吗？
没有普适定律。linear scaling 是经验起点，Transformer/AdamW 仍需验证 warmup、stability 和 loss curve。

### Q11. Checkpoint 应该保存哪些状态？
- model；
- optimizer；
- scheduler；
- scaler（适用时）；
- RNG；
- data position；
- step/epoch；
- config/version metadata。

### Q12. 为什么只保存 model weights 不能无缝 Resume？
optimizer moments、LR phase、random state、data cursor 丢失后，后续训练轨迹会改变。

### Q13. Reproducibility 为什么不等于每次 bitwise identical？
GPU kernel、distributed reduction、data loading 可能有非确定性。更实用目标是：配置、数据、seed、code 可追溯，结果在合理 variance 内可复现。

### Q14. Multi-seed 为什么重要？
小数据或 post-training 可能 seed variance 不小。单次提升 0.5 点未必超过随机波动。

### Q15. Checkpoint Frequency 怎么权衡？
越频繁恢复损失越小，但 I/O 和存储开销越大。大规模训练常结合 asynchronous/distributed checkpoint。

### Q16. EMA 适用于所有 LLM 训练吗？
不是。EMA 在视觉/生成模型常见，但标准 LLM pretraining 不一定使用。不能把某类模型的 recipe 当成通用规则。

### Q17. Training Run 的最小实验记录是什么？
```text
code commit
model config
data version + mixture
optimizer/scheduler
seed
hardware/world size
precision
checkpoint
metrics
```

### Q18. 训练异常首先看哪些曲线？
loss、grad norm、learning rate、tokens/s、GPU memory、per-domain loss、validation buckets。不要只盯总 loss。
