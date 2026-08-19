# 03_视觉token为什么拖慢推理

## 面试一句话

视觉 token 既增加视觉 encoder 计算，也增加 LLM prefill 序列长度。

## 核心回答

- 高分辨率 → 更多 patch → 更多 visual tokens。
- projector/token merge 只要能减少 N，就能显著减轻 LLM 侧成本。
- 视频尤其严重，因为 token 数还要乘帧数。
- 所以 2026 的模型架构越来越重视 token routing/compression。
