# 09 · Multimodal RAG, Tools, GUI & VLA

> 本页保留 **RAG / GUI / VLA 的应用层入口**。Agent 的底层循环、Planning、Memory、Multi-Agent、MCP/A2A、Agent RL、Sandbox、Checkpoint 和 Production Runtime 已独立放到：
>
> **[09B · Agent Fundamentals & Engineering](../09B_Agent_Fundamentals_Engineering/README.md)**。

## Q1. 普通 VQA 和 Multimodal Agent 的本质区别？

VQA：输入 → 回答。

Agent：

```text
感知
→ 状态理解
→ 规划
→ action/tool call
→ 环境变化
→ 再感知
→ 直到完成任务
```

关键是**闭环行动**，不是回答更长。

## Q2. Function Calling 本质是什么？

让模型从自然语言生成受 schema 约束的结构化调用：

```json
{"name":"search","arguments":{"query":"..."}}
```

系统执行函数，把结果写回上下文，再让模型继续推理。

## Q3. Function Call 是怎么训练出来的？

SFT 样本包含：

- tool schema；
- user request；
- correct tool call；
- tool result；
- final response。

复杂 agent 还需要 multi-step trajectory 和错误恢复样本。

## Q4. 为什么多模态 Function Calling 更难？

工具参数可能来自视觉：

- “点击图中右上角按钮”；
- “用 OCR 读取这个表格”；
- “搜索这张图里的产品”。

因此模型必须先 grounding，再产生正确工具参数。

## Q5. MCP 和普通 Function Calling 什么关系？

Function calling 是模型输出“调用哪个工具、参数是什么”的能力；MCP 更偏**标准化模型/Agent 与外部工具、资源和数据之间的连接层**。

面试可以先记：

```text
Function Calling = 模型侧动作决策
MCP              = Agent ↔ Tool/Resource 连接协议
A2A              = Agent ↔ Agent 协作协议
```

MCP/A2A 的 2026 版本和工程细节见 [09B](../09B_Agent_Fundamentals_Engineering/README.md)。

## Q6. Multimodal RAG 和 Text RAG 差在哪？

文档里有：

- 文本；
- 图片；
- 表格；
- chart；
- page layout。

只抽纯文本会丢视觉结构。多模态 RAG 常把 page image、text chunks、figures、tables 同时索引和返回。

## Q7. Multimodal RAG 的典型 pipeline？

```text
PDF / Web / Images
→ parse / render
→ chunk text + page/region
→ multimodal embeddings
→ retrieve
→ rerank
→ feed text + page images to MLLM
→ answer + citation
```

要分别评估 retrieval 和 generation，不要只看最终 QA。

## Q8. Embedding model 和 Reranker 有什么区别？

- Embedding：双塔，query/document 分别编码，向量检索快；
- Reranker：cross-encoder，query 和 candidate 共同编码，精度更高但更贵。

典型：先 embedding 召回 top-K，再 rerank top-K。

## Q9. 为什么多模态检索不能只把图片 caption 化？

Caption 是有损压缩，可能丢：

- 小字；
- 图表数值；
- 空间布局；
- 视觉风格；
- 未被 caption 提到的对象。

因此更强方案直接学习 image/document/video embedding。

## Q10. GUI Agent 的完整链路？

```text
Screenshot
→ UI understanding / OCR / grounding
→ plan
→ click(x,y) / type / scroll / key
→ new screenshot
→ verify
```

关键能力：视觉定位、动作格式、长期状态追踪、失败恢复。

## Q11. GUI grounding 如何训练？

数据可以来自：

- UI hierarchy / accessibility tree；
- screenshot + bounding box；
- synthetic web；
- human trajectory；
- automated exploration。

训练模型把自然语言目标映射到 bbox/point/action。

## Q12. GUI Agent 为什么不能只看 next-action accuracy？

一步预测对，不代表任务能完成。应看：

- task success；
- steps；
- invalid actions；
- recovery；
- latency/cost；
- safety。

最终指标是 end-to-end outcome。

## Q13. Web Agent 为什么需要 DOM + Screenshot 两种信息？

DOM：结构化、文字准确、元素 ID 清楚；Screenshot：能看到真实布局、图片、canvas、视觉状态。

两者结合通常比只用一种更鲁棒。实际任务中要根据 token 成本决定是否同时使用。

## Q14. Agent memory 有哪些层次？

- working memory：当前上下文；
- episodic memory：过去任务/轨迹；
- semantic memory：长期知识/RAG；
- environment state：外部世界当前状态。

更完整的 memory write/compaction/external state 见 [09B](../09B_Agent_Fundamentals_Engineering/README.md)。

## Q15. Agent Planning 常见策略？

- ReAct：reason → act → observe；
- plan-then-execute；
- hierarchical planning；
- tree/search；
- tool-first routing；
- learned policy。

简单任务不一定需要复杂 planning，额外思考会增加延迟。完整 planner/executor/verifier 设计见 [09B](../09B_Agent_Fundamentals_Engineering/README.md)。

## Q16. VLA 是什么？

Vision-Language-Action 模型把输出从文本扩展到动作：

```text
视觉观测 + 语言指令
→ policy/model
→ action tokens / continuous control
```

用于机器人、自动驾驶/操作、具身智能。

## Q17. Action tokenization 怎么做？

连续动作可以：

- 离散 bin/token；
- vector regression；
- diffusion/action chunk；
- mixture distribution。

离散 token 易与 LLM 统一，但量化精度有限；连续输出更自然但训练头不同。

## Q18. 一个可靠 Agent 系统如何防止一步错到底？

加入闭环：

1. action 前检查；
2. action 后读取新状态；
3. verifier 判断是否朝目标推进；
4. 异常时 retry/replan；
5. 高风险动作请求确认；
6. 设置最大步数和 rollback。

Agent 的可靠性来自 **model + environment feedback + guardrails**。

---

## 下一步

如果这一页能讲清，再进入 [09B Agent Fundamentals & Engineering](../09B_Agent_Fundamentals_Engineering/README.md)，重点补：

**Tool Runtime → Planning → Memory → Multi-Agent → MCP/A2A → Coding Agent → Agent RL → Evaluation → Sandbox / Durable Execution。**
