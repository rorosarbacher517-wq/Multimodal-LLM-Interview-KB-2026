# 02_手写masked_SFT_loss

## 面试一句话

多模态 SFT 通常只让 assistant 输出部分计算 CE loss。

## 核心回答

- labels 中不需要学习的位置置为 -100。
- PyTorch CrossEntropyLoss 默认 ignore_index=-100。

## 代码 / 公式

```python
labels = input_ids.clone()
labels[user_and_image_positions] = -100
loss = torch.nn.functional.cross_entropy(
    logits[:, :-1].reshape(-1, logits.size(-1)),
    labels[:, 1:].reshape(-1),
    ignore_index=-100
)
```
