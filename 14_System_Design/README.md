# 14 · Multimodal System Design

> 系统设计题统一按：**需求/SLO → 数据流 → 模型 → 检索/工具 → serving → 评测 → 风险/降级**。

## Q1. 设计一个企业 PDF 多模态问答系统

```text
PDF
→ page render + text/layout parse
→ text/page/table/image chunks
→ multimodal embedding
→ vector retrieval
→ rerank
→ page images + text evidence
→ MLLM
→ answer + page citation
```

关键：表格和图不能只 OCR 成纯文本；要保留 page/region evidence。

## Q2. 设计电商“以图搜商品”

- image encoder 得 query embedding；
- product image/text 预计算 embedding；
- ANN recall；
- multimodal reranker；
- business filters：库存、类目、价格；
- final ranking。

指标：Recall@K、NDCG、CTR/CVR、latency。

## Q3. 设计长视频 QA

先做视频索引：

```text
shot split
→ frame/clip embeddings
→ timestamps + transcript + OCR
→ query retrieval
→ top clips 高 FPS 重编码
→ MLLM reasoning
```

避免整小时视频一次进入模型。

## Q4. 设计 GUI Agent

```text
screenshot/DOM
→ grounding/OCR
→ planner
→ action executor
→ new state
→ verifier
→ retry/replan
```

高风险动作：支付、删除、发送邮件前必须加 policy/confirmation。

## Q5. 设计实时语音视频助手

至少拆服务：

- VAD / audio stream；
- video frame scheduler；
- audio/video encoder；
- LLM/Thinker；
- speech decoder/Talker；
- session memory；
- interruption controller。

核心 SLO：first audio latency、interruption latency、RTF。

## Q6. 设计多模态内容审核系统

两阶段：

1. cheap classifiers/vision rules 高吞吐筛查；
2. MLLM 对复杂语境、OCR、图文组合做深度判断。

加：policy versioning、human escalation、false positive/negative audit。

## Q7. 设计模型数据生产平台

```text
source registry
→ distributed ingestion
→ parse/decode
→ quality filters
→ dedup
→ model scoring
→ safety/PII
→ shards + metadata
→ mixture builder
→ training feedback
```

必须有 lineage：任何训练样本能追到来源、版本和过滤步骤。

## Q8. 设计一个多模态 RAG 服务如何降低成本？

- 先 text/image embedding cheap recall；
- 只对 top-K 用 MLLM reranker；
- page/vision embedding cache；
- query routing：纯文本问题不调用视觉模型；
- dynamic resolution；
- batch vision encoding。

## Q9. 设计视觉模型 A/B 实验

控制：

- prompt；
- image resolution；
- decoding；
- traffic bucket；
- latency budget。

指标同时看质量和成本，避免 A 只是因为用了 4×视觉 token 所以更准。

## Q10. 设计一个 8GB GPU 上的本地 VLM

优先：

- 小语言 backbone；
- 强但轻量 vision encoder；
- visual token compression；
- 4-bit weight quantization；
- GQA/小 KV；
- 限制 max resolution/images；
- llama.cpp/MLX 等端侧 runtime（按平台）。

## Q11. 设计多租户 MLLM Serving

需要：

- request admission；
- per-tenant quota；
- image/video size limits；
- token budget；
- continuous batching；
- cache isolation；
- priority queue；
- overload degradation；
- metrics + billing。

## Q12. 设计视觉 Agent 的安全机制

三层：

1. **Perception**：OCR/grounding confidence；
2. **Policy**：高风险 action block/confirm；
3. **Execution**：sandbox、least privilege、rollback、audit log。

不要把安全完全交给 prompt。

## Q13. 设计一个“上传图片后自动生成结构化 JSON”的服务

- image preprocess；
- MLLM extraction；
- JSON schema constrained decoding；
- validator；
- retry with error feedback；
- low-confidence human review。

评测：field-level precision/recall，不只看 JSON 是否 parse。

## Q14. 设计一个视觉模型 bad-case 闭环

```text
online logs
→ sample/cluster failures
→ human taxonomy
→ reproduce
→ root cause
→ data/model fix
→ regression set
→ retrain
→ shadow/A-B
```

bad case 进入训练前先进入**独立 regression set**，避免“修了以后就没法客观测”。

## Q15. 系统设计最后应该主动补什么？

主动讲 trade-off：

- accuracy vs latency；
- visual detail vs tokens；
- model size vs concurrency；
- caching vs freshness/privacy；
- agent autonomy vs safety。

能讲 trade-off 才像真正做过系统，而不是画组件图。