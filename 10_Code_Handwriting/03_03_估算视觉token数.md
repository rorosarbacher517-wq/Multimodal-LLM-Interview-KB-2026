# 03_估算视觉token数

## 面试一句话

面试时先用 patch 近似估算，再说明实际模型可能 merge/resize。

## 核心回答

- 固定 ViT：N≈(H/P)×(W/P)。
- 视频再乘 frame 数 T。
- 动态分辨率模型要先根据 resize/tile 规则计算 H',W'。

## 代码 / 公式

```python
def vit_tokens(h, w, patch=14, frames=1):
    return (h // patch) * (w // patch) * frames
```
