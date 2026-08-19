# 11 · Inference & Serving Optimization

## Q1. LLM 推理分哪两个阶段？

- **Prefill**：处理整个输入 prompt，生成 KV cache；
- **Decode**：每一步生成新 token，并复用过去 KV。

多模态还多一个 vision/audio encoder preprocessing 阶段。

## Q2. 多模态请求的 latency 怎么拆？

```text
media download/decode
+ image/video preprocess
+ vision encoder
+ projector
+ LLM prefill
+ decode
+ network/queue
```

只看 tokens/s 很可能忽略图片解码和视觉 encoder。

## Q3. 为什么视觉 token 会让 Prefill 特别慢？

视觉 token 增加总 `L`。Dense attention 的计算随序列增长很快，而且每个视觉 token 还会经过多层 LLM。

所以减少 `N_visual` 往往比只优化 vision encoder 更能影响端到端成本。

## Q4. KV Cache 显存怎么估算？

近似：

```text
KV bytes =
B × L × layers × n_kv_heads × head_dim × 2 × bytes_per_elem
```

GQA/MQA 通过减少 `n_kv_heads` 降低 cache。

## Q5. Continuous Batching 是什么？

传统 batch 要等一组请求一起结束。continuous batching 在 decode 过程中不断加入新请求、移除完成请求，提高 GPU 利用率和吞吐。

这是 vLLM/SGLang 等 serving engine 的核心思想之一。

## Q6. PagedAttention 解决什么问题？

KV cache 长度动态变化，直接连续分配容易碎片化、浪费显存。PagedAttention 类似虚拟内存分页，把 KV 分成 blocks/pages，按需映射，提高 cache 利用率和 batching 灵活性。

## Q7. Prefix Caching 什么时候有效？

多个请求共享长前缀，例如：

- 相同 system prompt；
- 相同文档；
- 相同多轮历史；
- 相同图片 embedding（若框架支持 multimodal cache）。

缓存已有 prefix KV/feature 可以跳过重复 prefill。

## Q8. Speculative Decoding 是什么？

小 draft model 先猜多个 token，大 model 一次验证；接受的 token 可以批量前进。

加速条件：

- draft 足够快；
- 接受率高；
- verification 实现高效。

视觉输入主要影响 prefill，因此 speculative decoding 主要优化生成阶段。

## Q9. FlashAttention 优化了什么？

数学上仍然是 exact attention，但通过 tiling 把 Q/K/V 分块放进片上 SRAM，减少 HBM 读写，不显式存完整 attention matrix。

它优化的是 **IO 和 kernel efficiency**，不是把理论 attention 直接变成线性复杂度。

## Q10. FlashAttention-3/4 的面试重点？

- FA3：针对 Hopper 的异步执行、warp specialization、FP8 等硬件能力；
- FA4：进一步面向 Blackwell 重构 pipeline、memory movement 和 softmax 等。

核心思想：attention kernel 要和 GPU 架构共同设计。

FA4 source: [arXiv:2603.05451](https://arxiv.org/abs/2603.05451)

## Q11. INT8、INT4 权重量化为什么能省显存？

FP16 权重 2 bytes/param；INT8 约 1 byte；INT4 理论约 0.5 byte，再加 scale/metadata。

权重量化主要减少：

- model memory；
- decode 权重读取带宽。

精度损失取决于模型、层、校准方法。

## Q12. GPTQ 和 AWQ 怎么简单区分？

两者都是常见 post-training weight quantization 路线。

- GPTQ：基于二阶近似/逐层误差最小化思想；
- AWQ：强调 activation-aware，保护对输出重要的权重通道。

面试无需死背实现细节，但要知道它们主要是**无需完整重新训练的权重量化**。

## Q13. KV Cache 也可以量化吗？

可以。长上下文下 KV 可能比权重还成为显存大头。

但 KV 会被每步 attention 读取，对量化误差和 kernel 支持敏感，需要在 quality、memory、speed 间验证。

## Q14. vLLM 如何支持多模态请求？

典型链路：

- processor 解析 text/image/video/audio；
- media encoder 产生 feature；
- 将 multimodal feature 与 text sequence 对齐；
- engine 做调度和生成。

线上必须限制每请求的图片/视频和视觉 token 数，避免单请求拖垮 batch。

官方：[vLLM multimodal inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs/)

## Q15. SGLang 和 vLLM 面试怎么比较？

不要简单说“谁更快”。可从：

- scheduler；
- prefix/cache；
- structured generation；
- distributed serving；
- multimodal support；
- kernel/backend；
- ecosystem compatibility。

具体性能必须在同模型、同硬件、同 workload benchmark。

## Q16. TTFT 和 TPOT 是什么？

- **TTFT**：Time To First Token，主要受 queue + preprocess + vision + prefill 影响；
- **TPOT**：Time Per Output Token，主要反映 decode。

聊天产品重 TTFT；长文本生成也很关心 TPOT。

## Q17. Throughput 和 Latency 为什么冲突？

大 batch 能提高 GPU 利用率和吞吐，但请求排队更久、单请求 latency 可能上升。

Serving 的目标是满足 SLO 下最大吞吐，而不是纯追求 GPU 利用率 100%。

## Q18. 多模态模型如何做缓存？

可分层缓存：

- media bytes / decoded image；
- vision preprocessing；
- vision embeddings；
- LLM prefix KV；
- retrieval results。

同一图片被多次提问时，缓存视觉 embedding 很有价值，但要考虑模型版本、resize 参数和安全隔离。

## Q19. Vision Encoder 和 LLM 可以分开部署吗？

可以，尤其当两部分计算特征差异很大：

```text
Vision GPU pool
→ projected visual embeddings
→ LLM GPU pool
```

好处是独立扩缩容和负载平衡；代价是跨节点传 feature、调度复杂、缓存一致性。

InternVL3.5 的 DvD 是公开相关例子。

## Q20. 线上 MLLM OOM 怎么排查？

顺序：

1. 单请求 visual token 是否异常；
2. max context / max images / video frames；
3. KV cache block 使用；
4. concurrent sequences；
5. model weight/quantization；
6. vision feature cache；
7. fragmentation；
8. TP size。

真正有效的第一步通常是**打印每个请求的 text tokens + visual tokens + KV 占用**。