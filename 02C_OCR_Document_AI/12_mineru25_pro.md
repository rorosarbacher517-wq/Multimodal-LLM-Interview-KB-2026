# MinerU2.5 / MinerU2.5-Pro：Coarse-to-Fine Document Parsing

## 面试一句话

MinerU2.5 的关键设计是 **低分辨率看全局 layout，高分辨率 crop 看局部内容**；2026 的 MinerU2.5-Pro 进一步强调数据工程和后训练，而不是只换模型架构。

## MinerU2.5

```text
Downsampled page
→ global layout analysis
→ native-resolution crops
→ local content recognition
→ structured document
```

这样避免所有高分辨率像素都进入大模型。

## MinerU2.5-Pro 的面试价值

公开报告强调：

- difficulty-aware data sampling；
- cross-model consistency verification；
- judge-and-refine annotation；
- progressive training / GRPO alignment。

说明 Document AI 的瓶颈越来越多来自 **数据覆盖与标注质量**。

## References

- MinerU2.5: https://arxiv.org/abs/2509.22186
- MinerU2.5-Pro: https://arxiv.org/abs/2604.04771
- Repo: https://github.com/opendatalab/MinerU