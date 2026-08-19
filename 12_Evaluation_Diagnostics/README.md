# 12 · Evaluation & Diagnostics

> Agent 的 end-to-end success、partial completion、recovery、cost、safety、OSWorld/BrowserGym 和 trajectory-level diagnosis 见 **[Agent Evaluation & Diagnostics](./AGENT_EVAL.md)**。

## Q1. 为什么不能用一个 benchmark 判断 MLLM 强不强？

多模态能力是多维的：

- general VQA；
- OCR/document；
- math/diagram reasoning；
- grounding；
- multi-image；
- video；
- hallucination；
- agent/GUI；
- latency/cost。

一个综合分数会掩盖明显短板。

## Q2. MMMU 主要测什么？

MMMU 是多学科、多模态理解与推理 benchmark，包含大学/专业领域的图表、图像、示意图问题。

它更偏**综合知识 + visual reasoning**，不是专门 OCR 或 grounding benchmark。

## Q3. MathVista / MathVision 主要测什么？

视觉数学推理：图表、几何、科学图、视觉条件下的数学问题。

失败要区分：

1. 数字/图形没看清；
2. 关系理解错；
3. 数学推理错。

## Q4. OCR benchmark 应该怎么拆？

至少分：

- character/word recognition；
- scene text；
- document OCR；
- reading order；
- table；
- formula；
- OCR-based QA。

只测最终 QA 无法知道 OCR 本身是否正确。

## Q5. Document QA 怎么评估更合理？

从 pipeline 拆：

- page retrieval；
- text/layout recognition；
- table/chart extraction；
- answer accuracy；
- citation/page evidence。

长文档还要测跨页引用和上下文长度鲁棒性。

## Q6. Grounding 用什么指标？

- bbox IoU；
- point accuracy；
- recall/precision；
- normalized coordinate error；
- referring expression success。

GUI 场景最终还要看 click 是否落到真实可交互区域。

## Q7. Video QA 除 accuracy 还要看什么？

- temporal grounding；
- long-video retrieval；
- event ordering；
- frame sampling sensitivity；
- FPS/token budget；
- latency。

同一模型用 8 帧和 128 帧的结果不能直接当作同成本比较。

## Q8. 多模态 hallucination 是什么？

模型生成视觉证据中不存在或无法支持的内容，例如：

- 不存在的物体；
- 错误颜色/数量；
- 错误空间关系；
- 图表里不存在的数值。

它不是普通 factual hallucination 的简单复制，而是**视觉 grounding failure**。

## Q9. 如何测模型是否真的在看图？

做 counterfactual test：

- 换图但保持问题；
- 擦掉关键区域；
- crop/zoom；
- image shuffle；
- text-only baseline；
- adversarial language prior。

如果答案几乎不变，模型可能主要依赖语言 shortcut。

## Q10. 如何区分 Perception Error 和 Reasoning Error？

让模型先输出或用工具验证中间视觉事实：

```text
Step 1: OCR / objects / coordinates
Step 2: reasoning
```

如果 Step 1 错，是 perception；Step 1 对但 final 错，是 reasoning。还可用人工标注或 specialized detector 验证。

## Q11. Benchmark contamination 怎么诊断？

- 检索训练语料 exact match；
- n-gram / MinHash；
- image perceptual hash；
- embedding nearest-neighbor；
- benchmark release time 之后的数据隔离；
- 对相似题改图/改数做 perturbation。

高得异常但改写后掉很多，可能存在记忆风险。

## Q12. Agent benchmark 为什么最容易被评测脚本骗？

Agent 成功依赖环境状态，单纯字符串 match 不够。

应该验证：

- 最终环境状态；
- 文件/网页是否真的变化；
- action side effects；
- 安全约束；
- 是否利用 evaluator bug。

完整 Agent 评测见 [Agent Evaluation & Diagnostics](./AGENT_EVAL.md)。

## Q13. Offline Eval 和 Online Eval 怎么配合？

Offline：快速、稳定、便于回归。

Online/A-B：真实用户分布，能发现 benchmark 不覆盖的问题。

推荐：

```text
unit eval → capability benchmark → shadow traffic → A/B → monitoring
```

## Q14. 线上 MLLM 监控哪些指标？

质量：

- task success；
- hallucination/complaint；
- tool error；
- safety。

系统：

- TTFT；
- TPOT；
- vision encode latency；
- tokens/request；
- GPU utilization；
- OOM/retry；
- cost/request。

## Q15. 如何设计一套自己的 Evaluation Suite？

1. 按业务能力分桶；
2. 每桶真实 hard cases；
3. 固定 versioned test set；
4. 自动 + 人工评分；
5. 记录模型/参数/prompt/resolution；
6. 每次训练做 regression；
7. 线上 bad case 回灌，但避免污染原 test。

## Q16. 面试问“模型提升了 2 个点，你相信吗？”怎么答？

先问：

- 样本量；
- confidence interval；
- seed variance；
- prompt/decoding 是否一致；
- image resolution 是否一致；
- test contamination；
- cost 是否增加；
- 是否多个 benchmark 同方向。

只有 controlled comparison 才能把提升归因到方法本身。
