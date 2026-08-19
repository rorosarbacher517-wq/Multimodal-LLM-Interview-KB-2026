# 16C · Agent 高频面试题

> 用法：先闭卷口述 1–3 分钟。说不清，再回到 [09B Agent Fundamentals & Engineering](../09B_Agent_Fundamentals_Engineering/README.md)。

## A. Agent 基础
1. Agent 和普通 Chatbot 的本质区别是什么？
2. Agent 和 Workflow 的边界怎么判断？
3. 一个最小 Agent Loop 包含哪些组件？
4. Observation、State、Action 分别是什么？
5. 为什么 Agent 必须有 Stop Condition？
6. 什么任务不适合做成 Agent？
7. Planner / Executor / Verifier 为什么要拆？
8. Agent 为什么强调 closed-loop，而不是一次性生成完整计划？

## B. Tool Use
9. Function Calling 本质是什么？
10. Tool Schema 为什么会直接影响成功率？
11. Tool Description 应该写哪些信息？
12. Tool Routing 怎么做？
13. 工具太多为什么会让 Agent 变差？
14. Parallel Tool Calling 什么时候安全？
15. Tool Result 为什么不能全部原样塞回上下文？
16. Timeout / Retry / Backoff 怎么设计？
17. Idempotency 为什么对支付、邮件、删除操作特别重要？
18. Tool Error 为什么最好结构化返回？

## C. Planning / Reasoning
19. ReAct 是什么？
20. ReAct 和 Plan-then-Execute 的区别？
21. Hierarchical Planning 为什么适合长任务？
22. Reflection 为什么有时没用？
23. Verifier 为什么比“再思考一次”更可靠？
24. Outcome Reward 和 Process Reward 区别？
25. 为什么 Planning 越复杂不一定越好？
26. 什么时候应该触发 Replan？

## D. Context / Memory
27. Agent 的 Context Engineering 是什么？
28. Working / Episodic / Semantic / Procedural Memory 怎么区分？
29. 长上下文为什么不等于长记忆？
30. Memory Write Policy 为什么重要？
31. Context Compaction 如何避免丢约束？
32. Externalized State 为什么有利于长任务？
33. Context Drift 是什么？
34. 长任务如何避免重复执行已经完成的动作？

## E. Multi-Agent / Protocol
35. 什么时候值得做 Multi-Agent？
36. Manager–Worker 是什么？
37. Handoff 和 Tool Call 有什么区别？
38. Shared Memory Multi-Agent 有哪些一致性问题？
39. MCP 是什么？
40. A2A 是什么？
41. Function Calling、MCP、A2A 三者怎么区分？
42. 协议标准化解决什么，不能解决什么？
43. 一个 Agent 怎么发现远程 Agent 的能力？

## F. Web / GUI / Coding Agent
44. Web Agent 为什么常同时需要 DOM 和 Screenshot？
45. GUI Agent 的 action space 有哪些？
46. GUI grounding 为什么是 computer-use 的关键？
47. Coding Agent 和 Code Completion 的区别？
48. Coding Agent 为什么一定要有测试/验证闭环？
49. Sandbox 为什么是 Coding Agent 的基础设施？
50. Research Agent 为什么不能只看“搜索数量”？
51. Multimodal Agent 为什么会把 perception error 放大成 action error？
52. Agent 和 VLA 的关系是什么？

## G. Agent Training / RL
53. Agent trajectory 数据应该保存什么？
54. Agent SFT 和普通 QA SFT 的区别？
55. Agent RL 为什么更像真正的 sequential decision making？
56. Credit Assignment 为什么在长任务里困难？
57. Sparse Reward 怎么缓解？
58. Synthetic trajectory 如何防止“假成功”？
59. Curriculum Agent Training 怎么设计？
60. Environment rollout 为什么是 Agent RL 的主要成本之一？

## H. Evaluation / Reliability
61. Agent 最重要的指标为什么通常是 end-to-end task success？
62. Step Accuracy 为什么不能代表 Agent 真正能力？
63. OSWorld / OSWorld 2.0 主要测什么？
64. Web Agent 为什么需要可执行环境评测？
65. Agent failure taxonomy 怎么拆？
66. Agent trace 至少应该记录什么？
67. 如何评价 retry 能力和 recovery 能力？
68. 如何做 cost-normalized Agent evaluation？
69. 为什么 long-horizon benchmark 比短任务更容易暴露状态丢失？

## I. Safety / Production
70. Prompt Injection 为什么对 Agent 比对普通 Chatbot 更危险？
71. Least Privilege 怎么落地？
72. Human-in-the-Loop 应该插在哪些动作之前？
73. Harness 和 Sandbox 为什么要分离？
74. Durable Execution 是什么？
75. Checkpoint / Resume 应该保存哪些状态？
76. Agent Runtime 怎么做 timeout / cancellation？
77. 多 Agent 系统怎么防止循环调用？
78. 如何给 Agent 做预算控制？
79. Agent Observability 为什么必须做到 trajectory level？
80. 如何设计一个可部署、可恢复、可审计的 Agent 系统？

---

## 面试通过标准

至少做到：
- 2 分钟讲清 Agent Loop；
- 画出 Tool Use + State + Verifier；
- 区分 Function Call / MCP / A2A；
- 能解释 Memory、Planning、Retry、Checkpoint；
- 能设计 Web/GUI/Coding Agent；
- 能从 task success、latency、cost、safety 四个方向评估系统。
