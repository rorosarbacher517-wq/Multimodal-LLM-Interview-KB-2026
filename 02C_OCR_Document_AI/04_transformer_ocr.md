# TrOCR / PARSeq：Transformer OCR 怎么做

## 面试一句话

Transformer OCR 把文字识别从“CNN + RNN + CTC”进一步改成视觉编码 + sequence decoding，使模型能利用更强的全局上下文。

## 两条典型路线

### TrOCR

```text
Image → ViT-like encoder → visual tokens → autoregressive text decoder
```

直接生成字符/token 序列。

### PARSeq

通过 permutation language modeling 训练，兼顾自回归和并行解码思想，提升上下文建模能力。

## 和 CTC 的区别

- CTC 假设输出顺序与输入时间步单调对齐；
- autoregressive decoder 可以显式利用已生成字符上下文；
- Transformer 通常更强，但计算和训练成本更高。

## References

- TrOCR: https://arxiv.org/abs/2109.10282
- PARSeq: https://arxiv.org/abs/2207.06966