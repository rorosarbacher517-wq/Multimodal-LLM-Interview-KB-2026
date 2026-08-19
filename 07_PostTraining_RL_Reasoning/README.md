# 07 · Post-training, RL & Multimodal Reasoning

## Q1. SFT、DPO、RLHF、RLVR 分别解决什么？

- **SFT**：学习正确示范和格式；
- **DPO**：从 preference pair 学偏好；
- **RLHF**：通过 reward model / human preference 优化 policy；
- **RLVR**：用程序/规则/环境等可验证奖励直接强化正确策略。

关系不是互斥，常按阶段组合。

## Q2. DPO 的直观原理？

给定 preferred `y+` 和 rejected `y-`，DPO 直接拉高 policy 对好答案相对坏答案的概率，同时以 reference policy 控制偏移。

优点：不需要显式训练 reward model + online rollout；缺点：依赖 preference pair 覆盖度，属于离线偏好学习。

## Q3. Reward Model 是怎么训练的？

输入 prompt + response，输出 scalar reward。常用 pairwise ranking loss，使：

```text
r(chosen) > r(rejected)
```

多模态 reward model 必须看到图像/视频，否则可能只根据语言风格判断，无法识别“答案是否忠于视觉”。

## Q4. PPO 在 RLHF 中为什么复杂？

它包含：

- rollout；
- reward；
- advantage estimation；
- policy/value optimization；
- KL control。

大模型上 rollout 本身就非常贵，训练/推理引擎同步也是工程难点。

## Q5. GRPO 的核心思想？

对同一 prompt 采样一组 responses，根据组内 reward 相对位置构造 advantage，而不必依赖传统 value model。

直观：

```text
同一道题生成 K 个答案
→ verifier/reward 打分
→ 好的相对增强，差的相对抑制
```

常用于 reasoning post-training。

## Q6. RLVR 为什么特别适合数学、代码和 GUI？

因为奖励可自动验证：

- 数学：final answer / symbolic checker；
- 代码：unit test；
- grounding：IoU / point accuracy；
- GUI：环境最终状态；
- tool call：执行是否成功。

自动 verifier 能大规模生成稳定反馈。

## Q7. 多模态 RL 最大难点是什么？

最终答案错可能有两种来源：

1. **没看清图**；
2. **看清了但推理错**。

如果 reward 只看 final answer，模型可能用语言先验蒙对，也可能无法知道 perception 哪一步需要改。

## Q8. 如何设计视觉 reasoning reward？

可组合：

- final answer reward；
- grounding/region reward；
- OCR exact-match；
- format reward；
- tool-use success；
- consistency / verifier reward；
- trajectory-level environment reward。

奖励越多不一定越好，要防止 reward conflict 和 hacking。

## Q9. 什么是 Reward Hacking？

模型学会优化奖励规则，而不是任务本身。例如：

- 输出格式刚好骗过 parser；
- 利用 evaluator 漏洞；
- 生成超长模板获得 style reward；
- GUI 中触发表面 success 标志但没有完成真实目标。

解决：多 verifier、随机化、环境级检查、人工 audit。

## Q10. Multimodal CoT 为什么可能有效？

对图表、几何、复杂场景，显式中间步骤有助于拆解：

```text
识别视觉事实
→ 建立关系
→ 计算/推理
→ 答案
```

但长 CoT 不等于好 reasoning；如果第一步视觉事实错，后面只会把错误讲得更长。

## Q11. “Thinking 更长”为什么不一定更好？

视觉任务中模型可能长时间在语言空间自我推演，却没有重新检查图像。2025–2026 的研究开始强调 **lookback / re-grounding / active perception**。

面试回答：视觉 reasoning 的关键是**每一步是否锚定视觉证据**，不是 token 数。

## Q12. Test-time scaling 是什么？

训练模型不变，推理时投入更多计算：

- longer thinking；
- self-consistency；
- Best-of-N；
- verifier rerank；
- tree/search；
- 主动 crop/zoom/retrieve。

目标是按任务难度动态分配计算。

## Q13. Best-of-N 有什么优缺点？

对同一问题采样 N 个答案，由 reward/verifier 选最好。

优点：简单、容易并行。

缺点：成本线性增加，而且 verifier 如果不可靠，N 越大越可能找到“骗过 verifier”的答案。

## Q14. Self-consistency 和 Best-of-N 区别？

- Self-consistency：通常按答案多数投票/一致性；
- Best-of-N：用独立 reward/verifier 选最大分。

前者需要答案可归一化，后者依赖 evaluator 质量。

## Q15. Visual Grounding 为什么是 reasoning 的基础？

因为它把语言实体绑定到具体视觉区域。没有 grounding，模型容易出现：

- object hallucination；
- left/right 错；
- 数量错；
- GUI 点击错位置。

复杂 reasoning 可以把 grounding 作为显式中间步骤或工具。

## Q16. Active Perception 是什么？

模型不是一次性看完固定图像，而是在推理中决定：

- zoom 哪；
- crop 哪；
- 取视频哪个时间段；
- 调 OCR / detector；
- 请求更高分辨率。

它把视觉 token budget 从“平均分配”变成“按问题动态分配”。

## Q17. Cascade RL 这类多阶段 RL 为什么有意义？

不同阶段优化难度不同。先用较稳定的 offline/curated feedback 建基本策略，再在线 rollout 做更细 alignment，可以减轻直接大规模 online RL 的不稳定和成本。

是否优于单阶段必须由实验验证；InternVL3.5 是公开案例之一。

## Q18. Curriculum RL 是什么？

训练环境从简单到困难逐步变化，例如：

```text
single-step VQA
→ multi-step reasoning
→ grounding + reasoning
→ tool use
→ long-horizon GUI task
```

目标是控制 exploration 难度和 reward sparsity。

## Q19. 为什么 Agent RL 比普通 QA RL 难？

Agent reward 通常延迟很长：前 20 步都可能没有明确分数，最后才知道任务成功与否。

还存在：

- environment stochasticity；
- credit assignment；
- action invalid；
- trajectory 很长；
- rollout 成本高。

因此需要 trajectory verifier、shaping reward、异步 rollout infrastructure。

## Q20. 面试问“如何让模型少看图瞎猜”怎么答？

从链路回答：

1. 数据：增加 counterfactual、hard negative、grounding；
2. 训练：视觉依赖的 SFT/RL reward；
3. 架构：高分辨率、多层视觉特征；
4. 推理：lookback / crop / visual tool；
5. 评测：区分 perception vs reasoning error；
6. 产品：低置信度触发二次视觉检查。

这比只说“加 RLHF”完整得多。