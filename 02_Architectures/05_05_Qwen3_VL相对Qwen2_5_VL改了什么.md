# 05_Qwen3_VL相对Qwen2_5_VL改了什么

## 面试一句话

Qwen3-VL 的公开架构更新重点包括 Interleaved-MRoPE、DeepStack 和更精细的视频时间对齐。

## 核心回答

- Interleaved-MRoPE：更系统地处理 time/height/width 位置维度。
- DeepStack：把 ViT 多层特征送入语言模型，减少只依赖最后一层视觉语义导致的细节损失。
- Text–Timestamp Alignment：加强视频事件与时间戳的对应。
- 同时提供 Dense/MoE、Instruct/Thinking 等不同配置。
## 易错点

- 不要把 Qwen3-VL 的公开模块细节推广到闭源模型。

## 参考

- https://github.com/QwenLM/Qwen3-VL
