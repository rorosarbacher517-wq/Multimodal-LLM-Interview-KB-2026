# 07 Advanced · RL Math & Rollout Infrastructure

> 补齐 PPO / GAE / DPO / GRPO 的数学直觉与工程链，不要求背长推导，但要知道每一项解决什么。

### Q1. Policy Gradient 的基本式子？
直觉上提高高 reward action/sequence 的 log-probability：
```text
∇J ≈ E[A · ∇ log π(a|s)]
```
`A` 表示这个 action 比 baseline 好多少。

### Q2. 为什么需要 Baseline / Advantage？
直接用 return 方差很大。减去 baseline 后不改变期望方向，但能降低 variance。

### Q3. Value Function 是什么？
估计状态未来期望 return，用于构造 advantage。PPO-RLHF 常额外训练 value model/head。

### Q4. GAE 的直觉？
Generalized Advantage Estimation 在 bias 与 variance 之间通过 `λ` 做折中，把多步 TD residual 加权累积。

### Q5. PPO Clip Objective 解决什么？
限制新 policy 相对旧 policy 一次更新过大：
```text
r_t = π_new / π_old
clip(r_t, 1-ε, 1+ε)
```
避免 reward signal 把策略一步推崩。

### Q6. RLHF 中为什么加 KL Penalty？
约束 policy 不要离 reference/SFT model 太远，减少语言质量崩坏和 reward hacking。

### Q7. DPO Objective 的直觉？
直接让 policy 对 chosen 相对 rejected 的 log-probability gap 比 reference 更大，无需显式 online PPO rollout。

### Q8. DPO 的局限？
训练只覆盖离线 preference pairs；如果数据没有覆盖新的 policy failure，它不会主动探索环境。

### Q9. GRPO 为什么可以不训练 Value Model？
同一 prompt 采样一组 outputs，用组内 reward 均值/方差构造相对 advantage，减少单独 value network 的需求。

### Q10. Reward Normalization 为什么重要？
不同 task/reward scale 差异太大时，一个 reward source 会支配梯度。常需要 normalization/clipping/weight tuning。

### Q11. Sequence-level Reward 怎么分配到 Token？
最简单是整条 response 共享 terminal advantage；更细可使用 process reward / step reward，但标注和 verifier 更难。

### Q12. On-policy 和 Off-policy 区别？
- on-policy：用当前 policy rollout，分布匹配但成本高。
- off-policy：利用旧数据，效率高但有 distribution mismatch。

### Q13. Rollout Engine 为什么是大模型 RL 的瓶颈？
需要大量生成：
```text
prompts → N responses → verifier/reward → advantages → train
```
生成经常比 backward 更耗 wall-clock，需要独立 inference workers 和异步 pipeline。

### Q14. Asynchronous RL 有什么好处和风险？
好处：rollout 与 training overlap；风险：rollout policy 变旧，产生 policy staleness。

### Q15. Multimodal Verifier 应看到什么？
如果任务依赖图像，verifier 也应获得必要视觉证据，或者使用可验证结构（OCR exact match、IoU、环境 state），否则会只奖励语言风格。

### Q16. Process Reward 与 Outcome Reward 区别？
- outcome：只看最终成功。
- process：给中间步骤反馈。

process reward 可改善 credit assignment，但错误的 step label 也会强行塑造不可靠 reasoning。

### Q17. Reward Hacking 怎么用实验发现？
- 手工 inspect 高 reward 低真实质量样本；
- adversarial verifier tests；
- reward vs human score correlation；
- increase sample count 看是否出现 exploiting patterns。

### Q18. RL 实验至少记录哪些系统指标？
rollout tokens/s、accept/success rate、reward distribution、KL、entropy、response length、GPU utilization、policy lag、verifier latency。
