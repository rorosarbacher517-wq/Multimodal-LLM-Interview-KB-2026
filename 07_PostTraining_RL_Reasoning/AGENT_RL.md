# Agent RL & Sequential Decision Making

> Agent RL 的核心不是“把 GRPO 用到 Agent 上”，而是：**模型的动作会改变环境，奖励往往延迟，轨迹很长，执行成本高。**

## Q1. 为什么 Agent 更像 MDP / POMDP？
可以抽象为：

```text
state s_t
→ policy π(a_t | observation/history)
→ action a_t
→ environment
→ s_{t+1}
→ reward r_t
```

GUI/Web/真实世界通常只能看到部分状态，因此更接近 POMDP。

## Q2. Agent RL 和单轮 QA RL 最大区别？
单轮 QA 常是：prompt → response → reward。

Agent 是：

```text
state → action → state → action → ... → outcome
```

前一步会改变后续输入分布。

## Q3. 为什么 Agent Reward 常常很稀疏？
很多任务只有最后才能判断：
- 文件是否改对；
- 订单是否完成；
- 软件是否配置成功。

中间几十步可能没有天然 reward。

## Q4. Reward Shaping 是什么？
给中间状态增加辅助奖励，例如：
- 找到正确页面；
- 通过一个子测试；
- 完成 subgoal。

优点：降低探索难度；缺点：可能把模型带向“刷中间分数”。

## Q5. Credit Assignment 为什么难？
最终失败可能来自很早的一步错误。

需要判断：

```text
哪一步 action
真正导致后续不可恢复？
```

可结合 verifier、subgoal、process label、trajectory analysis。

## Q6. Agent RL 为什么需要 Environment Rollout Infrastructure？
训练样本不是静态文本，而要真实执行：
- 启动浏览器/容器；
- 执行动作；
- 返回 observation；
- 保存状态；
- 重置环境。

环境吞吐常成为训练瓶颈。

## Q7. 为什么 rollout worker 和 trainer 常解耦？
rollout 偏 inference/environment I/O；trainer 偏大规模 backward。

异步架构可以：

```text
rollout workers → trajectory queue → trainer
```

提高硬件利用率，但要处理 policy staleness。

## Q8. On-policy 和 Off-policy Agent Data 有什么区别？
- On-policy：当前 policy 自己生成轨迹；
- Off-policy：历史模型、人类、teacher 的轨迹。

Off-policy 数据便宜，但和当前 policy 分布可能不同。

## Q9. Agent 可以做 DPO 吗？
可以对完整 trajectory 或关键 decision 构造 preferred / rejected pairs。

例如：
- 成功轨迹 > 失败轨迹；
- 5 步高效完成 > 20 步绕路；
- 安全动作 > 危险动作。

但 pair 要可比较。

## Q10. GRPO 类方法如何用于 Agent？
可以对同一 task rollout 多条 trajectory：

```text
same task
→ K trajectories
→ environment/verifier reward
→ relative advantage
→ update policy
```

真正难点在 rollout 成本和 reward 质量，而不只是公式。

## Q11. Outcome Verifier 有哪些类型？
- unit test；
- DOM/environment state check；
- file diff；
- database state；
- simulator success；
- human approval。

最好直接验证环境，不只用 LLM judge。

## Q12. Process Verifier 有什么价值？
可判断某一步：
- tool 是否合理；
- action 是否非法；
- reasoning 是否违反约束。

但 process label 成本更高，也更容易把人为偏好写死。

## Q13. Reward Hacking 在 Agent 中有哪些例子？
- 修改测试脚本让测试“通过”；
- 点击表面 success 元素但未完成业务；
- 删除失败日志；
- 利用 evaluator bug。

所以 verifier 需要隔离和防篡改。

## Q14. Agent RL 为什么特别需要 Sandbox？
在线探索会主动尝试不同动作。如果环境连接真实生产：
- 可能删除数据；
- 发送真实邮件；
- 产生费用。

训练环境必须隔离、可 reset、可 snapshot。

## Q15. Curriculum Agent RL 怎么做？

```text
single tool
→ two-step tool
→ multi-step workflow
→ partial failure
→ recovery
→ long horizon
→ multi-agent
```

逐渐增加 horizon 和环境复杂度。

## Q16. Exploration 在 Agent 中怎么理解？
模型需要尝试未验证路径，但过多探索会增加成本和风险。

可通过：
- sampling temperature；
- multiple rollouts；
- task randomization；
- search/planning；
- uncertainty-triggered exploration。

## Q17. Agent RL 如何训练 Stop Behavior？
Premature stop 和 endless loop 都是常见问题。

reward 可以同时考虑：
- success；
- step cost；
- unnecessary tool calls；
- timeout；
- explicit stop correctness。

## Q18. 为什么要给 Tool Call 加 Cost Penalty？
如果 reward 只看成功，模型可能调用 100 次工具完成一个简单任务。

可优化：

```text
utility = success_reward - λ * tool_cost - μ * latency
```

但 penalty 太强会让模型不敢用必要工具。

## Q19. Multi-Agent RL 多了什么困难？
- credit 在 agent 之间分配；
- communication cost；
- non-stationary teammates；
- coordination failure；
- shared reward ambiguity。

## Q20. Agent RL 的离线诊断应该看什么？
不要只看平均 reward。还看：
- success by task bucket；
- steps；
- tool usage；
- failure stage；
- retry/recovery；
- unsafe actions；
- reward-model disagreement；
- rollout cost。

## Q21. Agent RL 训练闭环怎么画？

```text
task pool
→ environment rollout
→ trajectory
→ executable verifier / reward
→ advantage / preference
→ policy update
→ new rollout
```

如果 reward 不能可信反映真实 outcome，后面算法再复杂也没有意义。
