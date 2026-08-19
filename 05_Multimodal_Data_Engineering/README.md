# 05 · Multimodal Data Engineering

> 对模型数据岗，最重要的不是“我会清洗数据”，而是能从**能力目标 → 数据定义 → 生产 → 训练反馈 → 再迭代**讲完整闭环。
>
> Agent 的 trajectory schema、environment rollout、recovery data、tool schema versioning、executable verification 单独见 **[Agent Data Engineering](./AGENT_DATA.md)**。

## Q1. 多模态大模型训练数据有哪些大类？

- image-text pairs；
- interleaved image-text documents；
- OCR / document / table / chart / formula；
- grounding / detection / region caption；
- multi-image reasoning；
- video-caption / temporal QA / timestamp grounding；
- audio / speech / audiovisual；
- GUI / web / app trajectory；
- tool use / agent environment trajectory；
- synthetic reasoning / verifier-generated data。

## Q2. 数据工程从哪里开始？

不是先“爬数据”，而是先定义**能力桶**：

```text
能力目标
→ 可观测错误
→ 需要什么监督信号
→ 去哪里找数据
→ 如何验收
```

例如 OCR 差，不是无脑加 image-caption，而是增加小字、文档、表格、reading order 等数据。

## Q3. 图文数据采集后第一轮清洗做什么？

四层：

1. 文件可读性：损坏、格式、极端尺寸；
2. 基础质量：分辨率、模糊、空白、重复；
3. 文本质量：乱码、广告、过短、模板垃圾；
4. 跨模态一致性：图和文字是否真的匹配。

## Q4. 多模态去重和文本去重有什么不同？

需要同时看：

- exact file hash；
- perceptual hash（视觉近重复）；
- image embedding similarity；
- text MinHash / n-gram / embedding；
- image-text pair 级组合去重。

只按 URL 去重远远不够，因为同一图可能被不同网站重新编码。

## Q5. 为什么 benchmark contamination 特别危险？

如果测试图、题目、答案或近似版本进入预训练/SFT，benchmark 会虚高。

需要：

- exact match；
- n-gram / MinHash；
- image perceptual hash；
- embedding near-duplicate；
- 时间截断；
- benchmark-specific blacklist。

## Q6. 图文匹配质量如何自动打分？

可组合：

- CLIP/SigLIP similarity；
- caption completeness；
- OCR-text consistency；
- object/entity overlap；
- teacher VLM judging；
- rule-based quality features。

不要只用一个分数硬阈值，最好做多特征质量模型或分桶。

## Q7. 数据配比怎么设计？

不能按原始数据量直接混合。步骤：

1. 定义 capability buckets；
2. 设初始 sampling weight；
3. 训练；
4. 看各 bucket loss / benchmark / bad cases；
5. 上调短板、下调过拟合或低收益桶；
6. 迭代。

这就是 data mixture optimization。

## Q8. 为什么高质量小数据可能比海量弱数据更重要？

后训练阶段尤其如此。低质量 instruction 会教模型错误格式、幻觉和 shortcut。高质量数据能提供更清晰的梯度方向。

但预训练仍需要规模和覆盖度，所以**规模和质量不是二选一，而是不同阶段权重不同。**

## Q9. OCR / 文档数据要额外处理什么？

- page rendering DPI；
- text box / reading order；
- table structure；
- formula；
- page number / section hierarchy；
- 小文字可读性；
- 多页关联。

单纯“PDF 转纯文本”会丢掉大量视觉结构。

## Q10. 视频数据怎么采样？

不能固定只说“每秒一帧”。要根据任务：

- coarse understanding：均匀采样；
- short event：高 FPS / event-aware；
- long video：shot segmentation + retrieval；
- temporal grounding：保留真实 timestamp；
- action task：关键动作前后密集采样。

## Q11. Agent / GUI 数据是什么形态？

典型 trajectory：

```text
state/screenshot
→ instruction
→ reasoning(optional)
→ action(click/type/scroll/tool)
→ new state
→ reward/success
```

训练重点不只是 next action，还包括长期任务成功与错误恢复。更完整的 schema/rollout/verifier 见 [Agent Data Engineering](./AGENT_DATA.md)。

## Q12. 合成多模态数据怎么生产？

三类常用方式：

- Teacher model 生成 caption/QA/reasoning；
- 程序化生成 chart/geometry/table/GUI，可得到精确标签；
- 环境 rollout 生成 agent trajectories。

随后用 verifier、规则、多模型一致性、执行结果过滤。

## Q13. 合成数据最大的风险？

- teacher hallucination；
- 风格同质化；
- 模型学会 synthetic shortcut；
- 错误 reasoning trace 被放大；
- 训练分布离真实用户过远。

所以 synthetic data 需要真实数据锚定和持续 bad-case audit。

## Q14. 如何做数据价值评估？

最可靠不是看“数据看起来好不好”，而是做训练反馈：

- small-scale controlled training；
- per-domain ablation；
- influence / gradient proxy；
- quality score vs downstream gain；
- marginal gain per token / per GPU-hour。

数据策略最终要回答：**这批数据带来了什么能力增量？**

## Q15. 为什么要做训练反馈驱动的数据闭环？

静态清洗规则无法知道模型下一阶段缺什么。闭环：

```text
训练 → benchmark/bad case
→ 错误分类
→ 缺口数据寻源/合成
→ 过滤/配比
→ 再训练
```

这是数据工程从 ETL 升级成 model-aware data engineering 的核心。

## Q16. 面试被问“如何生产 10 亿条多模态数据”怎么答？

按工程链回答：

1. source registry + licensing；
2. distributed crawler / ingestion；
3. media decoding；
4. rule filtering；
5. dedup；
6. model-based scoring；
7. PII/safety；
8. shard/metadata/version；
9. sampling mixture；
10. data lineage + experiment tracking；
11. 训练反馈重新打分。

重点是**可复现、可追踪、可增量更新**，不是只有几个清洗函数。
