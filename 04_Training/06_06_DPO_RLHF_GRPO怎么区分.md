# 06_DPO_RLHF_GRPO怎么区分

## 面试一句话

SFT 学“怎么回答”；偏好优化学“哪种回答更好”；RLVR/GRPO 可直接用可验证奖励强化推理策略。

## 核心回答

- DPO：直接从 preference pair 优化，无需显式 reward model rollout。
- RLHF：常见流程是 reward model + policy optimization。
- GRPO：用同一 prompt 多个样本的组内相对奖励构造 advantage，常用于 reasoning。
- 多模态 RL 的难点是奖励必须区分“看错了”和“推理错了”。
