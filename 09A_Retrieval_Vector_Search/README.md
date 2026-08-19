# 09A · Retrieval, Vector Search & RAG Engineering

> `09 RAG/Agents` 讲完整系统，本模块补齐检索底层：**BM25 → Embedding → ANN → HNSW/IVF/PQ → Hybrid Retrieval → Reranking → RAG Evaluation**。

---

### Q1. Sparse Retrieval 和 Dense Retrieval 区别？
- sparse：基于词项匹配，例如 BM25，关键词精确、可解释。
- dense：把 query/document 编码为向量，用语义相似度检索。

真实 RAG 常组合两者。

### Q2. BM25 的直觉是什么？
词在文档中出现越多通常越相关，但会饱和；全库很常见的词价值低；同时对文档长度做归一化。

不要求面试手背完整公式，但要懂 **TF saturation + IDF + length normalization**。

### Q3. Bi-Encoder 为什么适合大规模 Recall？
Query 和 document 独立编码，document vector 可预计算：

```text
q_emb @ doc_embs
```

因此可以用 ANN index 做百万/十亿级搜索。

### Q4. Cross-Encoder / Reranker 为什么更准但更贵？
Query 和 candidate 一起输入模型，能做细粒度 token-level interaction；但每个 candidate 都要重新 forward。

典型 pipeline：`ANN top100 → reranker top10`。

### Q5. Cosine、Dot Product、L2 Distance 怎么选？
如果 embedding 已 L2 normalize：

```text
cosine ranking ≈ dot-product ranking
```

具体 index metric 必须与模型训练目标一致。

### Q6. Exact Search 为什么无法无限扩展？
每个 query 与所有向量做相似度计算，复杂度随 corpus N 线性增长。大库需要 Approximate Nearest Neighbor。

### Q7. HNSW 的直觉？
构建多层小世界图：上层快速远距离跳转，下层局部精细搜索。

主要超参影响：
- recall；
- memory；
- build time；
- query latency。

### Q8. IVF 的直觉？
先用 coarse centroids 把向量分桶，query 只搜索最相关的若干 inverted lists，而不是全库。

### Q9. Product Quantization (PQ) 在做什么？
把高维向量切成多个子空间，每个子空间用 codebook 近似编码，从而大幅压缩 index memory。

代价是距离近似误差。

### Q10. HNSW 和 IVF-PQ 怎么选？
- HNSW：高 recall、查询快，但内存较大。
- IVF-PQ：更适合超大库和内存受限场景，但调参/量化误差更明显。

应基于真实 corpus 和 SLO benchmark。

### Q11. Hybrid Retrieval 是什么？
融合 BM25 与 dense retrieval，例如：
- score fusion；
- Reciprocal Rank Fusion；
- 两路召回后 union + rerank。

能同时覆盖专有名词和语义改写。

### Q12. Multimodal Retrieval 索引什么？
可以同时存：
- text chunk embedding；
- page-image embedding；
- figure/table embedding；
- video clip embedding；
- metadata filters。

### Q13. Chunk Size 为什么会影响 RAG？
太小：上下文不完整；太大：embedding 语义被稀释、返回内容浪费 context。

文档最好结合 heading、page、layout 等结构切块。

### Q14. Query Rewriting 有什么用？
把用户自然语言问题转成更适合 retrieval 的查询，例如补全实体、拆 multi-hop 子问题、生成关键词。

但 rewrite 错了也会降低 recall，所以要保留原 query 或做多路检索。

### Q15. Hard Negative 是什么？
看起来很像正确答案、但实际上不相关的 candidate。用 hard negatives 训练 embedding/reranker，比随机 negatives 更能提升边界能力。

### Q16. Reranker 怎么训练？
常见：
- pointwise relevance score；
- pairwise preferred vs rejected；
- listwise ranking objective。

训练数据质量通常比模型尺寸更关键。

### Q17. Recall@K 为什么是 Retrieval 的第一层指标？
如果正确证据根本没进入 top-K，后面的 MLLM 再强也无法基于它回答。

### Q18. RAG 最终答案错了怎么定位？
分层：
1. parsing/chunking；
2. retrieval recall；
3. reranking；
4. context assembly；
5. generation；
6. citation correctness。

### Q19. Metadata Filter 为什么重要？
时间、权限、语言、文档类型、tenant 等条件可以在向量检索前/后过滤，减少无关结果并保证 ACL。

### Q20. RAG Cache 可以缓存什么？
- query embedding；
- retrieval result；
- rerank result；
- parsed page/vision embeddings；
- final answer（谨慎处理 freshness）。

### Q21. RAG 为什么要做 Versioning？
文档、embedding model、chunking、index、reranker 任一变化都可能改变结果。线上必须能追溯：

```text
corpus_version + embedding_version + index_version + prompt/model_version
```

### Q22. 面试设计 RAG 的推荐回答模板？

**Corpus → parse/chunk → sparse+dense index → recall → rerank → evidence assembly → MLLM → citation → eval → monitoring/security**。
