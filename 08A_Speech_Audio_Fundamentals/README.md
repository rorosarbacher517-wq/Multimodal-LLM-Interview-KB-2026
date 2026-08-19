# 08A · Speech & Audio Fundamentals

> `08 Video/Audio/Omni` 负责多模态实时系统；本模块补齐语音算法本身：**waveform → acoustic representation → ASR/audio understanding → speaker → codec → TTS → streaming**。

---

### Q1. Waveform、Spectrogram、Mel Spectrogram 区别？
- waveform：时间域振幅。
- spectrogram：短时傅里叶变换后的 time-frequency 表示。
- Mel spectrogram：把频率轴映射到更接近人类听觉感知的 Mel scale。

### Q2. 为什么语音通常要分 Frame？
语言信号在很短时间窗内可近似平稳。常通过 window + hop 把长 waveform 分成局部帧处理。

### Q3. ASR 在做什么？

```text
audio → acoustic encoder → text tokens
```

困难包括口音、噪声、多人说话、专有名词、实时延迟。

### Q4. CTC ASR 的核心思想？
模型每个时间步输出 token/blank，通过对重复和 blank 路径求和，在没有 frame-level 字符对齐的情况下训练。

### Q5. Seq2Seq / Transducer ASR 与 CTC 有什么不同？
- seq2seq：decoder 基于 encoder feature 和历史 token 自回归生成。
- RNN-T/Transducer：适合 streaming，联合 acoustic time 与 label history。
- CTC：结构简单、条件独立假设更强。

### Q6. Whisper 路线为什么影响大？
大规模弱监督 speech data + Transformer encoder-decoder，把 ASR、translation、language identification 等统一成 seq2seq token prediction。

### Q7. wav2vec 2.0 的核心是什么？
先在未标注 waveform 上做 self-supervised representation learning，再用较少标注数据 fine-tune ASR。

### Q8. WER 怎么算？

```text
WER = (Substitution + Deletion + Insertion) / Number of reference words
```

中文等语言也常看 CER。

### Q9. VAD 是什么？
Voice Activity Detection 判断什么时候有人说话。实时 agent 用它做：
- speech segment；
- turn detection；
- 降低无效 audio compute。

### Q10. Speaker Diarization 是什么？
回答“谁在什么时候说话”：

```text
audio → speech segments → speaker embeddings/clustering → speaker timeline
```

### Q11. Speaker Verification 和 Diarization 区别？
- verification：两段声音是不是同一个人。
- diarization：长音频里把多个说话人分开并标时间。

### Q12. Audio Event Classification 是什么？
识别非语音声音，例如门铃、车辆、玻璃破碎、音乐。Omni model 不能只等同于 ASR。

### Q13. Audio Codec Token 是什么？
神经 codec 把 waveform 压成离散 codebook indices。模型可以预测这些 token，再由 decoder 还原语音。

### Q14. 为什么会有多个 Codebooks？
单一 codebook 容量有限。Residual Vector Quantization 可以逐层编码剩余信息，提高音质，但生成/同步更复杂。

### Q15. TTS 的完整链路？
典型思路：

```text
text → linguistic/acoustic model → acoustic representation / codec
→ vocoder/decoder → waveform
```

现代 speech-to-speech 模型也可能直接生成 codec tokens。

### Q16. Vocoder 是什么？
把 spectrogram/latent/codec representation 转回 waveform，例如 WaveNet/HiFi-GAN 类模块解决最后的声学合成。

### Q17. Streaming ASR 为什么比 Offline ASR 难？
未来 audio 还没到，模型只能看有限右上下文。要权衡：
- latency；
- accuracy；
- chunk size；
- context cache。

### Q18. Endpointing 和 VAD 一样吗？
VAD 判断当前是否是 speech；endpointing 判断“一轮用户发言是否结束”。后者还会用 pause duration、语言语义、turn-taking cues。

### Q19. Full-duplex 里最难的不是 ASR 准确率，是什么？
模型要边听边说，同时处理：
- interruption；
- echo/自己的声音；
- turn-taking；
- audio/video sync；
- streaming state。

### Q20. Speech Latency 怎么拆？

```text
audio capture
+ VAD/chunk wait
+ encoder
+ LLM reasoning
+ speech token generation
+ decoder/playback buffer
```

### Q21. Audio 与 Text Token Rate 为什么不能直接对齐？
Audio 每秒原始采样点/feature frame 远多于文本 token，需要 encoder/codec 压缩和时间对齐，否则 context 很快爆炸。

### Q22. 多模态音频评测应该看什么？
- ASR：WER/CER；
- speaker：DER/EER；
- audio classification accuracy/mAP；
- TTS：intelligibility、speaker similarity、quality；
- streaming：first-audio latency、RTF、interruption latency。

## Primary references
- wav2vec 2.0: https://arxiv.org/abs/2006.11477
- Whisper: https://arxiv.org/abs/2212.04356
- HiFi-GAN: https://arxiv.org/abs/2010.05646
