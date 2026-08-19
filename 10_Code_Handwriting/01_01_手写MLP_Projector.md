# 01_手写MLP_Projector

## 面试一句话

最小多模态 projector 就是把视觉 hidden size 映射到 LLM hidden size。

## 核心回答

- 输入 `[B,N,Dv]`，输出 `[B,N,Dl]`。
- 常见是 Linear-GELU-Linear。

## 代码 / 公式

```python
import torch.nn as nn

class Projector(nn.Module):
    def __init__(self, d_v, d_l):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_v, d_l),
            nn.GELU(),
            nn.Linear(d_l, d_l),
        )
    def forward(self, x):   # [B, N, Dv]
        return self.net(x)  # [B, N, Dl]
```
