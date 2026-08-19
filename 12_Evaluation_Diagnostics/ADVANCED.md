# 12 Advanced · Statistics, Calibration & Robust Evaluation

### Q1. 为什么平均分不够？
需要知道 variance、confidence interval、不同 domain 的分布，以及提升是否来自少数 easy cases。

### Q2. Bootstrap Confidence Interval 怎么做？
从 test samples 有放回重采样多次，每次计算 metric，观察 metric distribution 的分位数作为区间。

### Q3. Paired Test 为什么比独立比较更有力？
A/B 模型在同一批样本上比较，可以直接看每个样本的差值，减少样本难度差异的噪声。

### Q4. 多个 Seed 为什么重要？
训练本身有随机性。小幅 gain 必须和 seed variance 比较，否则可能只是偶然。

### Q5. ECE 是什么？
Expected Calibration Error 把预测 confidence 分桶，比较 confidence 与真实 accuracy 的差距。

### Q6. Accuracy 高但 Calibration 差有什么问题？
如果模型错误时仍 99% confident，agent routing、human escalation 和 risk control 会很危险。

### Q7. Selective Prediction 是什么？
模型只在 confidence 足够高时自动回答，低置信度 abstain/调用工具/人工处理。要看 coverage–risk trade-off。

### Q8. OOD Evaluation 怎么设计？
按真实 shift 构造：新设备、新语言、新站点、新 UI、新天气/光照，而不是随机给图加噪声就叫 OOD。

### Q9. Robustness 与 Adversarial Robustness 一样吗？
Robustness 更广，包括自然分布变化、corruption、prompt variation；adversarial robustness 专指有目的优化的攻击扰动。

### Q10. Cost-normalized Evaluation 为什么重要？
模型 A 用 16× 更多视觉 token 得到 +1 分，不一定比 B 更好。应同时报告 latency、tokens、GPU-hour/cost。

### Q11. 一个 MLLM Benchmark Map 应怎么分桶？
- general/MMMU-style；
- OCR/document；
- chart/math；
- grounding；
- multi-image；
- video；
- hallucination；
- agent/GUI；
- safety；
- efficiency。

### Q12. Human Evaluation 什么时候不可替代？
开放生成、图像质量、helpfulness、复杂 agent trajectory 等很难完全规则化。但要有 rubric、多评审和一致性检查。

### Q13. LLM-as-a-Judge 有什么风险？
position bias、verbosity bias、self-preference、无法看见必要视觉证据、prompt sensitivity。应与人工/规则验证交叉校准。

### Q14. Regression Set 为什么不能持续回灌训练？
如果每次 bad case 都直接训练，原 regression set 会逐渐变成训练集，无法再客观测泛化。需要冻结 holdout 或不断构造新 blind set。

### Q15. 评测报告最少应记录什么？
```text
model checkpoint
processor/prompt/template
resolution/frame count
decoding/reasoning mode
dataset version
metric + CI
latency/token cost
failure buckets
```
