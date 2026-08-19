# 04_LoRA在MLLM里加哪里

## 面试一句话

LoRA 可以只加 LLM，也可以加 projector/vision tower；选择取决于你想改哪部分能力。

## 核心回答

- 只调 LLM：便宜，适合领域语言/指令。
- projector + LLM：更适合视觉语义分布变化。
- vision LoRA：适合医学、遥感、工业等视觉域偏移大场景。
- 部署时还要考虑 serving 框架是否支持 multimodal tower LoRA。
