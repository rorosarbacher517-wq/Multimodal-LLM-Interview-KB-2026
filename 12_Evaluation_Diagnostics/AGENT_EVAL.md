# Agent Evaluation & Diagnostics

> Agent 评测必须从“答案对不对”升级为**环境状态是否真的被正确改变**。

## Q1. Agent 的第一指标为什么通常是 Task Success？
因为 Agent 的目标是完成任务，而不是生成看起来合理的文字。

例如“创建文件并写入内容”，真正要检查：
- 文件是否存在；
- 内容是否正确；
- 路径是否正确。

## Q2. Binary Success 和 Partial Success 怎么配合？
Binary success 简单清楚，但长任务可能过于粗糙。

Partial score 可以按：
- completed subgoals；
- state changes；
- checklist coverage。

最终最好同时报告 binary + partial。

## Q3. 为什么 Step Accuracy 不够？
单步动作看起来合理，不代表：
- 长期目标完成；
- 没有绕路；
- 能从错误恢复；
- 最终状态正确。

## Q4. Agent Benchmark 为什么必须可执行？
如果只让另一个 LLM 判断轨迹，很容易被语言表面质量欺骗。

更可靠：

```text
agent action
→ real/simulated environment
→ state change
→ executable verifier
```

## Q5. Web / GUI Agent 的评测环境需要固定什么？
- 网站版本；
- initial state；
- account/data fixture；
- browser/device setting；
- screen resolution；
- timeout/max steps；
- network behavior。

否则 benchmark 会漂移。

## Q6. Agent Efficiency 怎么评？
同时记录：
- steps；
- model calls；
- tool calls；
- input/output tokens；
- wall-clock latency；
- monetary cost；
- environment reset cost。

## Q7. Recovery Ability 怎么测？
主动注入 failure：
- timeout；
- stale page；
- wrong tool result；
- permission denied；
- partial completion。

看模型是否能 detect → diagnose → retry/replan。

## Q8. Safety Evaluation 看什么？
- unauthorized action；
- prompt injection compliance；
- secret exfiltration；
- destructive operation；
- confirmation bypass；
- scope escalation。

## Q9. Prompt Injection Test 怎么构造？
把恶意指令放在：
- webpage；
- PDF；
- email；
- tool result；
- code comment；
- image OCR text。

看 Agent 是否把“外部数据”错误提升为高优先级 instruction。

## Q10. Agent Failure Taxonomy 为什么要按阶段拆？
建议：

```text
Perception
Retrieval
Planning
Tool Selection
Argument Generation
Execution
State / Memory
Verification
Safety
System Runtime
```

这样 bad case 才能对应数据、模型或系统修复。

## Q11. Agent Trace Review 应该看什么？
- 目标是否始终保持；
- 是否读到关键 observation；
- 工具是否合理；
- 是否重复动作；
- 是否错误停止；
- 是否忽略 verifier；
- 是否发生 context drift。

## Q12. Cost-Normalized Evaluation 为什么重要？
Agent A 成功率高 2%，但工具调用和 token 成本高 10 倍，生产价值未必更高。

可以画：

```text
success rate vs cost
success rate vs latency
success rate vs steps
```

## Q13. OSWorld / OSWorld 2.0 的价值是什么？
它们强调真实 computer-use 环境中的跨应用执行。OSWorld 2.0 进一步聚焦长周期工作流、动态状态和复杂约束。

- OSWorld: https://arxiv.org/abs/2404.07972
- OSWorld 2.0: https://arxiv.org/abs/2606.29537

## Q14. BrowserGym 为什么有价值？
它提供统一的 web-agent 环境接口与 benchmark 生态，便于在一致 observation/action setup 下比较 agent。

Primary: https://arxiv.org/abs/2412.05467

## Q15. Coding Agent 怎么评？
不只看 patch 文本：
- unit/integration tests；
- hidden tests；
- regression；
- diff scope；
- lint/typecheck；
- unsafe changes；
- task completion。

## Q16. Multi-Agent 怎么评？
除了最终成功率，还看：
- messages；
- handoffs；
- duplicated work；
- coordination failure；
- communication cost；
- individual agent contribution。

## Q17. Agent Online Monitoring 看什么？
质量：
- task success proxy；
- user correction；
- escalation；
- tool failure；
- unsafe action。

系统：
- p50/p95 latency；
- model/tool calls；
- token/cost；
- retries；
- timeout；
- sandbox failures。

## Q18. Agent A/B Test 最容易犯什么错误？
只比较 final success，却没有控制：
- tool set；
- max steps；
- budget；
- model version；
- environment state；
- retry policy。

Agent 实验必须做**system-level controlled comparison**。

## Q19. 如何判断 Agent 提升来自模型还是 Runtime？
做分层消融：

```text
same model + old runtime
same model + new runtime
new model + old runtime
new model + new runtime
```

再拆 planning、memory、tool schema、verifier、retry。

## Q20. 面试问“怎么评测一个 Agent？”怎么答？
按：

**environment reproducibility → end-to-end success → partial success → efficiency → recovery → safety → failure taxonomy → online monitoring**。
