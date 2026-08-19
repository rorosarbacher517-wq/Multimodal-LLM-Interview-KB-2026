# CRNN + CTC：经典文字识别链路

## 面试一句话

CRNN 把图像特征沿宽度方向转成序列，再用 CTC 在“不知道每个字符精确对齐位置”的情况下训练字符识别。

## 结构

```text
Text crop [B,3,H,W]
→ CNN feature [B,C,H',W']
→ squeeze height
→ sequence [B,W',C]
→ BiLSTM / sequence encoder
→ logits [B,W',V]
→ CTC loss
```

## CTC 为什么需要 blank

CTC 允许重复字符和空白路径，例如 `--b-oo-k-` 可以 collapse 成 `book`。

## 优点

- 不需要字符级对齐标注；
- 推理简单；
- 适合规则文本行。

## 局限

对复杂二维版式、极长文本和上下文语义利用有限。