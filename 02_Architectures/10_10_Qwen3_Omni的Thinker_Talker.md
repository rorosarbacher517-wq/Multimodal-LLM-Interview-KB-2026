# 10_Qwen3_Omni的Thinker_Talker

## 面试一句话

Qwen3-Omni 把“理解/推理”和“实时语音生成”拆成协作的 Thinker–Talker，使模型能同时处理 text/image/audio/video 并流式输出语音。

## 核心回答

- Thinker 负责多模态理解和语义推理。
- Talker 面向低延迟语音生成，并使用多 codebook 设计。
- Omni 模型的工程难点不只是模态数量，而是不同采样率、不同 token rate 和实时流式同步。
- 面试时要能解释为什么音频/视频不能简单当成一张超长图片。

## 参考

- https://github.com/QwenLM/Qwen3-Omni
