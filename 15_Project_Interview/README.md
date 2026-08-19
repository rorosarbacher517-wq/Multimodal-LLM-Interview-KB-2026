# 15 · Project Interview

## Q1. 一个算法项目应该怎么介绍？

推荐 90 秒结构：

```text
业务/科学问题
→ 数据规模和困难
→ baseline
→ 你的核心方法
→ 为什么这样设计
→ controlled experiment
→ 结果
→ bad case / limitation
→ 你个人负责什么
```

不要从“我们用了 Transformer”开始。

## Q2. 面试官问“为什么不用更简单的方法？”

先说 baseline，再说简单方法在哪个假设上失效，然后解释复杂方法只增加了什么必要能力。

好回答：

> “我先做了 XGBoost/MLP baseline。它在 A 场景已经足够，但 B 场景存在时间/空间依赖，所以才引入 Transformer。消融中只改变 backbone，增益为 …。”

## Q3. 如何证明提升来自你的模块？

做 paired/controlled ablation：

- 同数据；
- 同 split；
- 同训练 epoch；
- 同 backbone；
- 同 seed 或多 seed；
- 只改目标模块。

同时报告成本变化。

## Q4. 面试官问“数据怎么来的？”要说到什么程度？

不要只说来源名称。说完整：

```text
source
→ download/API
→ schema
→ parsing
→ QC
→ dedup
→ missing values
→ alignment
→ train/val/test split
→ versioning
```

数据工程本身就是算法可信度的一部分。

## Q5. 如何回答“你遇到最大的 bug？”

用排查过程展示工程能力：

1. symptom；
2. hypothesis；
3. instrumentation/log；
4. localization；
5. fix；
6. regression test；
7. prevention。

比说“显存不够，调小 batch”更有信息量。

## Q6. OOM 项目经历怎么讲？

先量化：

- 哪个 tensor 最大；
- shape；
- 为什么爆；
- 是 parameter、activation 还是 attention matrix。

再说 fix：chunking、checkpointing、mixed precision、token reduction、batching，并说明是否改变结果。

## Q7. 如何介绍一个多模态项目？

按模态流：

```text
image/video shape
→ encoder
→ feature shape
→ alignment/projector
→ text/other modality
→ fusion
→ prediction
→ loss
```

每一步说明维度和物理/业务含义。

## Q8. 面试官问“Transformer 在你的代码里到底怎么运行？”

不要背通用定义，要映射到你的 tensor：

- 一个 token 表示什么；
- sequence length 是什么；
- Q/K/V 在比较谁和谁；
- attention 输出如何进入 prediction；
- mask 是什么。

## Q9. 怎么讲模型失败案例？

分类而不是挑一个故事：

- data quality；
- OOD；
- perception；
- alignment；
- reasoning；
- long-tail；
- system latency/OOM。

然后说你用什么 evidence 确定根因。

## Q10. 如何回答“如果再给你两个月怎么改？”

不要说“换更大模型”。按 ROI 排：

1. 最确定的数据问题；
2. 最强 bad-case bucket；
3. 一个高收益架构/训练实验；
4. serving/成本；
5. 更严格 external validation。

## Q11. 项目里用了大模型 API，算不算算法项目？

取决于你做了什么。如果只是调用 API，算法含量弱；如果你完成：

- data construction；
- prompt/agent policy；
- retrieval；
- evaluator；
- fine-tuning；
- controlled experiment；
- cost/latency optimization；
- error analysis；

就可以形成完整算法/系统项目。

## Q12. 项目介绍最容易踩的坑？

- 把团队成果全部说成个人成果；
- 只讲模型名，不讲问题；
- 没 baseline；
- 没数据 split；
- 提升数字无法解释；
- 把 correlation 说成 mechanism；
- 遇到追问开始猜未验证细节。

最好的项目回答是：**边界清楚、数据清楚、实验清楚、贡献清楚。**