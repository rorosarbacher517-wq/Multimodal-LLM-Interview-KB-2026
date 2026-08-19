# 04_Test_Time_Scaling是什么

## 面试一句话

训练参数不变，在推理时投入更多计算，例如多次采样、反思、搜索、工具调用。

## 核心回答

- Self-consistency：多条 reasoning path 投票。
- Best-of-N：reward/verifier 选择最佳输出。
- Agentic search：主动 zoom/crop/retrieve video clip。
- 代价是延迟和成本，需要 adaptive compute，而不是所有请求都拉满。
