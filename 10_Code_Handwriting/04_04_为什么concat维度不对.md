# 04_为什么concat维度不对

## 面试一句话

最常见 bug 是把 `D_v` 的视觉 token 直接和 `D_l` 的文本 embedding 拼接。

## 核心回答

- 必须先 projector：`[B,N,Dv] -> [B,N,Dl]`。
- 再沿 sequence 维拼接，而不是 hidden 维。
- 即 `dim=1`，不是 `dim=-1`。

## 代码 / 公式

```python
vision = projector(vision)             # [B, Nv, Dl]
joint = torch.cat([text_left, vision, text_right], dim=1)
```
