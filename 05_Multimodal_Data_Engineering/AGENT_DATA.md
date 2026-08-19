# Agent Data Engineering

> Agent 数据不是普通 instruction-response。真正有价值的是**可执行环境中的状态—动作—反馈轨迹**。

## Q1. Agent 数据最基本的样本结构是什么？

```text
instruction
→ initial_state
→ observation_0
→ action_0
→ observation_1
→ action_1
→ ...
→ final_state
→ reward / verifier / success
```

如果只保存最终回答，就丢掉了 Agent 最关键的 sequential supervision。

## Q2. Agent trajectory 需要保存哪些字段？
建议至少：
- task_id / environment_id；
- instruction；
- state snapshot/reference；
- observation；
- available tools；
- tool schema version；
- action + arguments；
- tool result；
- timestamp；
- reward/verifier；
- final outcome；
- error/retry；
- model/prompt version。

## Q3. 为什么要保存 Available Tools？
同一 action 在不同工具集合下意义不同。训练时如果不知道当时模型能看到哪些工具，就无法判断：
- tool selection 是否正确；
- 是否出现 hallucinated tool；
- 是否存在 better alternative。

## Q4. Tool Schema 为什么必须 versioning？
API 参数会变化。旧 trajectory 里的：

```text
search(query, top_k)
```

可能和新版本不同。如果不记录 schema version，训练数据会出现“历史正确、当前非法”的调用。

## Q5. Agent 数据从哪里来？
常见来源：
- human demonstrations；
- production logs；
- expert/teacher rollout；
- scripted environment；
- synthetic task generation；
- self-play / multi-agent simulation；
- failure repair trajectory。

## Q6. Human Demonstration 的价值是什么？
真实人类轨迹能提供：
- 自然任务分解；
- 何时查询/确认；
- 错误恢复；
- 停止判断。

缺点是贵，而且人类操作不一定是最优 policy。

## Q7. Production Log 可以直接拿来训练吗？
不能。需要：
- PII/secret 清洗；
- 权限审计；
- bot/noise 过滤；
- success label；
- 去重；
- policy/version 对齐；
- consent/licensing。

线上日志是高价值数据，但也是高风险数据。

## Q8. Synthetic Task 怎么设计才有价值？
最好能**自动验证成功**。

例如：
- 生成一组文件并要求修改指定内容；
- 生成网页状态并要求完成表单；
- 生成数据库记录并要求查找/更新。

程序化环境比纯文本 teacher 更容易得到可靠 ground truth。

## Q9. 为什么 Synthetic Trajectory 必须执行？
Teacher 写：

> “任务已经成功完成。”

不代表环境真的成功。

必须：

```text
trajectory
→ replay / execute
→ environment verifier
→ keep / reject
```

## Q10. 如何生产 Recovery Data？
故意制造：
- tool timeout；
- wrong page；
- invalid parameter；
- stale state；
- permission denied；
- partial failure。

然后收集正确 recovery：retry / replan / ask user / fallback。

这类数据比只训练“完美轨迹”更接近真实系统。

## Q11. Negative Trajectory 有什么用？
可以训练模型识别：
- 错工具；
- 错参数；
- 重复动作；
- premature stop；
- unsafe action；
- unnecessary tool call。

可用于 preference data、reward model、verifier 或 DPO。

## Q12. Agent 数据如何去重？
不能只按 instruction 文本。

可以结合：
- normalized task state；
- tool sequence；
- action n-gram；
- environment snapshot hash；
- instruction embedding；
- final artifact hash。

## Q13. 为什么 Agent benchmark contamination 更复杂？
污染可能不是一条 question-answer，而是：
- task template；
- website snapshot；
- repository patch；
- hidden test；
- solution trajectory。

需要按 environment/task/repository 级别隔离。

## Q14. GUI Agent 数据要额外保存什么？
- screenshot；
- DOM/accessibility tree（若可用）；
- window/app metadata；
- screen resolution；
- click/drag coordinates；
- element bbox；
- post-action screenshot；
- success state。

坐标必须和分辨率/缩放保持一致。

## Q15. Coding Agent 数据要额外保存什么？
- repo commit/base SHA；
- file tree；
- inspected files；
- patch/diff；
- shell commands；
- test output；
- final git diff；
- verifier/test result。

否则无法可靠 replay。

## Q16. Multi-Agent 数据怎么记录？
需要把每个消息标注：

```text
sender_agent
receiver_agent
role / capability
shared_state_version
message/action
result
```

否则很难分析错误来自 manager、worker 还是通信。

## Q17. 如何做 Agent Data Quality Score？
可以分：
- task validity；
- trajectory executability；
- action legality；
- success；
- step efficiency；
- recovery quality；
- safety；
- diversity。

不要只让一个 LLM judge 给总分。

## Q18. Agent 数据配比怎么做？
按能力桶：
- single-tool；
- multi-tool；
- search/retrieval；
- GUI；
- coding；
- recovery；
- long-horizon；
- safety；
- multi-agent。

训练后根据 per-bucket success 和 bad case 调整 mixture。

## Q19. Agent 数据闭环怎么跑？

```text
online / benchmark failures
→ failure taxonomy
→ select high-value cases
→ human / teacher repair
→ executable verification
→ regression set first
→ training pool
→ retrain
→ re-evaluate
```

先进入 regression set，再进入训练，避免失去客观测试。

## Q20. 面试问“怎么做 Agent 数据生产平台？”怎么答？

```text
task generator / log ingestion
→ environment provisioning
→ rollout workers
→ trajectory storage
→ executable verifier
→ quality / safety filter
→ dedup / versioning
→ capability mixture
→ training
→ benchmark / online feedback
```

关键是 **environment reproducibility + trajectory lineage + verifier**。
