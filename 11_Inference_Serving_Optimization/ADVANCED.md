# 11 Advanced · Modern LLM/MLLM Serving

### Q1. Chunked Prefill 是什么？
把超长 prompt prefill 切成 chunks 调度，避免一个长请求长时间独占 GPU，也更容易和 decode requests 混合。

### Q2. Prefill/Decode Disaggregation 是什么？
把 compute-heavy prefill 与 memory-bandwidth-heavy decode 放到不同 GPU pools，分别扩缩容。

代价是 KV cache 需要跨节点传输/管理。

### Q3. Multimodal Disaggregation 还能怎么拆？
```text
media decode/preprocess pool
→ vision encoder pool
→ LLM prefill pool
→ decode pool
```
是否值得拆取决于流量、feature size 和 network overhead。

### Q4. Admission Control 为什么重要？
不是所有请求都能直接进入 GPU queue。需要根据 visual tokens、context、concurrency、tenant quota 预测 memory/cost，超限时拒绝、降级或排队。

### Q5. Scheduler 为什么要区分 Short / Long Request？
超长多图/视频请求会 head-of-line block 短聊天请求。可使用 priority、separate queue、token budget scheduling。

### Q6. Multi-LoRA Serving 是什么？
同一个 base model 动态加载/切换多个 LoRA adapters，为不同 tenant/task 服务，避免每个 adapter 都复制完整 base weights。

### Q7. LoRA Serving 的难点？
adapter cache、batch 内不同 adapter、kernel 支持、版本一致性和频繁加载 I/O。

### Q8. FP8 Serving 主要节省什么？
权重/activation 使用更低精度可减少 memory bandwidth 和提高 Tensor Core throughput，但需要硬件/kernel 支持和精度验证。

### Q9. SmoothQuant 的核心直觉？
把 activation 中难量化的 outliers 一部分“迁移”到 weight scale，使 activation/weight 更适合 INT8 quantization。

### Q10. TensorRT-LLM / Compiler Backend 的价值？
做 graph optimization、kernel fusion、quantization 和 hardware-specific scheduling。它与 vLLM/SGLang 的 scheduler/cache 层关注点不同但可有交集。

### Q11. Prefix Cache 失效条件有哪些？
model version、tokenizer/template、image preprocessing、position/rope config、adapter、权限 context 任一变化都可能让 cache 不可复用。

### Q12. Vision Feature Cache 的 Key 应包含什么？
不仅是 image hash，还应包含 processor/model version、resize/tile settings、possibly adapter/config。

### Q13. TTFT 过高怎么分解？
queue → media download/decode → vision encoder → projection → prefill → scheduling。先测各段 p50/p95/p99。

### Q14. TPOT 高怎么查？
看 batch size、KV bandwidth、quantization/kernel、TP communication、sampling overhead、speculative decoding acceptance。

### Q15. Serving Benchmark 为什么必须固定 Workload？
吞吐取决于 input/output length、image count、concurrency、arrival pattern、SLO。不同 workload 的“tokens/s”不能直接比较。

### Q16. MLLM 线上 Degradation Strategy 有哪些？
- 降 resolution/frame count；
- 限制多图数；
- 路由到小模型；
- 关闭 expensive tool/reasoning；
- 延迟低优先级请求。

前提是明确质量损失和业务边界。
