# 04_Multimodal_RAG怎么做

## 面试一句话

Multimodal RAG 不是只对图片做 caption 后检索；更完整的方案会同时索引文本、图像区域、文档页和结构化元数据。

## 核心回答

- 文档解析：page → text blocks/images/tables。
- embedding：文本/图像可用统一或双塔 embedding。
- retrieval：先粗召回，再用 MLLM rerank。
- generation：把相关页面/region 作为视觉证据送入模型。
- 要评估 retrieval recall 与 answer correctness 两个阶段。
