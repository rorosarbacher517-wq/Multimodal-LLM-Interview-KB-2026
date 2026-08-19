# 01_视频如何变成token

## 面试一句话

最直接方式是逐帧用视觉编码器，再把 frame tokens 加时间位置编码后送入 LLM；实际系统通常会强烈压缩。

## 核心回答

- T 帧 × N patch → T×N visual tokens，成本很快爆炸。
- 因此常用 frame sampling、temporal pooling、token merge、resampler。
- 短视频可密集采样；长视频需要分层摘要/检索。
