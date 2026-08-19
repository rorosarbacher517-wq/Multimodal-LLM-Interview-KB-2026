# 13 · Code Handwriting

> 面试目标不是背完整框架源码，而是能手写核心算子并解释 shape。

## Q1. 手写 Scaled Dot-Product Attention

```python
import math
import torch


def attention(q, k, v, mask=None):
    # q,k,v: [B, H, L, D]
    score = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    if mask is not None:
        score = score.masked_fill(mask == 0, float('-inf'))
    prob = torch.softmax(score, dim=-1)
    return prob @ v
```

关键：`[B,H,L,D] @ [B,H,D,L] → [B,H,L,L]`。

## Q2. 手写 Multi-Head reshape

```python
def split_heads(x, n_heads):
    B, L, D = x.shape
    d = D // n_heads
    return x.view(B, L, n_heads, d).transpose(1, 2)


def merge_heads(x):
    B, H, L, d = x.shape
    return x.transpose(1, 2).contiguous().view(B, L, H * d)
```

易错：transpose 后 `view` 前通常需要 `contiguous()`。

## Q3. 手写 causal mask

```python
def causal_mask(L, device):
    return torch.tril(torch.ones(L, L, device=device, dtype=torch.bool))
```

广播到 `[B,H,L,L]` 即可。

## Q4. 手写最简单 Vision Projector

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

    def forward(self, x):
        # [B, Nv, Dv] -> [B, Nv, Dl]
        return self.net(x)
```

## Q5. 怎么把视觉 token 插进文本 token？

概念代码：

```python
vision = projector(vision_feat)       # [B,Nv,D]
text = token_embedding(input_ids)     # [B,Nt,D]

joint = torch.cat(
    [text[:, :pos], vision, text[:, pos:]],
    dim=1
)
```

真实实现还要同步修改 attention mask、position ids、labels。

## Q6. 手写 masked SFT loss

```python
labels = input_ids.clone()
labels[not_assistant_mask] = -100

shift_logits = logits[:, :-1].contiguous()
shift_labels = labels[:, 1:].contiguous()

loss = torch.nn.functional.cross_entropy(
    shift_logits.view(-1, shift_logits.size(-1)),
    shift_labels.view(-1),
    ignore_index=-100,
)
```

核心是 causal shift + ignore non-target tokens。

## Q7. 手写 LoRA Linear

```python
class LoRALinear(nn.Module):
    def __init__(self, base, r=8, alpha=16):
        super().__init__()
        self.base = base
        self.r = r
        self.scale = alpha / r
        self.A = nn.Parameter(torch.randn(r, base.in_features) * 0.01)
        self.B = nn.Parameter(torch.zeros(base.out_features, r))

        for p in self.base.parameters():
            p.requires_grad = False

    def forward(self, x):
        return self.base(x) + (x @ self.A.T @ self.B.T) * self.scale
```

## Q8. 手写 ViT token 数估算

```python
import math

def n_patches(h, w, patch):
    return math.ceil(h / patch) * math.ceil(w / patch)
```

真实模型的 resize、patch merge 会改变结果，要按 processor 规则算。

## Q9. 手写 KV Cache 显存估算

```python
def kv_bytes(B, L, n_layers, n_kv_heads, head_dim, bytes_per_elem=2):
    return (
        B * L * n_layers * n_kv_heads * head_dim
        * 2  # K and V
        * bytes_per_elem
    )
```

面试时除以 `1024**3` 得 GiB。

## Q10. 手写 Top-k MoE Router 的核心

```python
def route(x, router, k=2):
    # x: [tokens, D]
    logits = router(x)                 # [tokens, E]
    prob = torch.softmax(logits, -1)
    weight, expert_id = torch.topk(prob, k, dim=-1)
    weight = weight / weight.sum(-1, keepdim=True)
    return expert_id, weight
```

真正实现难点在 token dispatch、capacity、all-to-all，不只是 topk。

## Q11. 手写简单 Image-Text Contrastive Loss 思路

```python
img = torch.nn.functional.normalize(img_emb, dim=-1)
txt = torch.nn.functional.normalize(txt_emb, dim=-1)
logits = img @ txt.T / temperature
labels = torch.arange(img.size(0), device=img.device)
loss_i = torch.nn.functional.cross_entropy(logits, labels)
loss_t = torch.nn.functional.cross_entropy(logits.T, labels)
loss = (loss_i + loss_t) / 2
```

## Q12. 动态分辨率 batch 怎么 collate？

三种思路：

```text
1. pad visual tokens + mask
2. flatten/pack + offsets
3. bucket by visual-token length
```

工程上常按 total token budget 做动态 batch。

## Q13. 手写 Gradient Accumulation 训练循环

```python
optimizer.zero_grad()
for step, batch in enumerate(loader):
    loss = model(**batch).loss / accum_steps
    loss.backward()

    if (step + 1) % accum_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

分布式时可用 `no_sync()` 避免每个 micro-step 都 all-reduce。

## Q14. 如何避免 softmax 数值溢出？

```python
x = x - x.max(dim=-1, keepdim=True).values
p = torch.exp(x)
p = p / p.sum(dim=-1, keepdim=True)
```

实际框架 softmax 已做稳定实现，但面试要知道 subtract-max 技巧。

## Q15. 代码题最常见的 shape 检查策略？

每个模块写出：

```text
input shape
→ operation
→ output shape
```

并 assert：

```python
assert D % n_heads == 0
assert vision.size(-1) == text.size(-1)
assert mask.shape[-1] == joint_seq_len
```

多模态 bug 很多不是算法错，而是 sequence length / mask / position id 没同步。