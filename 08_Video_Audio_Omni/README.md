# 08 · Video, Audio & Omni Models

## Q1. 视频输入最简单怎么变成 token？

```text
[B,T,3,H,W]
→ sample T' frames
→ vision encoder per frame
→ [B,T',N,Dv]
→ temporal/spatial compression
→ [B,N_video,Dl]
→ LLM
```

真正难点不是“多一个 T”，而是 **T×N** 会让 token 数快速爆炸。

## Q2. 为什么均匀采样视频帧不总可靠？

均匀采样适合全局语义，但可能错过持续 0.2 秒的关键事件。

更好的策略可能包括：

- scene/shot boundary；
- motion-aware；
- query-aware retrieval；
- coarse-to-fine sampling；
- event detector。

## Q3. 视频 position encoding 需要表达什么？

至少要区分：

- 时间 `T`；
- 高度 `H`；
- 宽度 `W`。

否则模型可以知道“左上角有什么”，却不一定知道“第 10 秒发生在第 20 秒之前”。

## Q4. Timestamp alignment 为什么重要？

视频 QA 常问“什么时候发生”。如果视觉帧只按内部 token position 排序，没有明确真实时间映射，模型很难稳定输出秒级时间。

因此可以把视觉帧与显式 timestamp token/text 对齐，让 `frame ↔ real time` 更直接。

## Q5. 长视频最大的三个瓶颈？

1. token 数；
2. 关键信息稀疏；
3. 跨长时间依赖。

所以完整方案通常是：

**压缩 + 检索 + 分层 memory + 必要时重新看局部片段。**

## Q6. 为什么长视频适合 Agentic Retrieval？

因为 1 小时视频里真正和问题相关的可能只有 20 秒。

Agent 可以：

```text
先读 coarse summary/index
→ 找候选时间段
→ 高 FPS 重看
→ 回答
```

比把所有帧一次塞给 LLM 更节省 token，也更不容易被无关信息干扰。

## Q7. 视频 token compression 有哪些方式？

- spatial pooling；
- temporal pooling；
- token merge；
- Resampler/Q-Former；
- keyframe selection；
- mixed compression ratio；
- learned router。

评价时要看：压多少 token、丢什么能力、压缩计算本身贵不贵。

## Q8. 音频模型如何把 waveform 变成 token？

常见链路：

```text
waveform
→ spectrogram / learned frontend
→ audio encoder
→ audio embeddings/tokens
→ projector/resampler
→ LLM
```

也可以使用离散 audio codec tokens。不同表示对 ASR、audio understanding、speech generation 的适合程度不同。

## Q9. ASR + LLM + TTS 和 end-to-end Omni 有什么区别？

串联系统：

```text
speech → text → LLM text → speech
```

优点：模块成熟、可控、易调试。

缺点：

- 丢语气、情绪、环境音；
- 多段延迟累积；
- 文字成为强信息瓶颈。

Omni 模型希望直接保留更多非文本声学信息，并统一流式交互。

## Q10. Speech tokenizer / codec token 是什么？

把连续音频压成离散 codebook token，模型可以像生成文本 token 一样生成语音表示，再交给 decoder/vocoder 还原 waveform。

多 codebook 可以提高声学信息容量，但生成同步更复杂。

## Q11. Full-duplex 为什么难？

全双工中模型需要同时：

- 听用户；
- 看视频；
- 更新状态；
- 说话；
- 判断用户是否打断；
- 必要时停止自己的输出。

因此它是**模型 + streaming runtime + turn-taking policy**的共同问题。

## Q12. Streaming 推理与普通 batch 推理区别？

普通 batch 可以等完整输入；streaming 必须不断接收 chunk：

```text
chunk1 → update cache/state
chunk2 → update
...
```

需要考虑：

- chunk size；
- cache；
- partial decoding；
- latency jitter；
- state reset；
- interruption。

## Q13. Omni 模型怎么做多模态同步？

不同模态的采样率完全不同：

- text：token/s；
- audio：高频帧/codec；
- video：fps；
- image：静态。

常见思想是各自 encoder/tokenizer 后，通过时间戳、共享时间轴、cross-modal alignment 或统一序列对齐。不能假设“一帧视频对应一个语音 token”。

## Q14. 视频/音频线上系统最重要的指标？

除了 accuracy：

- time-to-first-token / first-audio；
- end-to-end latency；
- real-time factor；
- interruption latency；
- dropped-frame rate；
- GPU utilization；
- memory/token cost；
- streaming stability。

实时产品里，低延迟往往与模型质量同样重要。