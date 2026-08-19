# 13 Advanced · High-value Handwriting Drills

> 每题重点是能解释 shape 和数值语义，不追求生产级 kernel。

## 1. RMSNorm
```python
import torch

def rmsnorm(x, weight, eps=1e-6):
    rms = x.pow(2).mean(dim=-1, keepdim=True).add(eps).rsqrt()
    return x * rms * weight
```

## 2. SwiGLU
```python
import torch.nn.functional as F

def swiglu(x, w_gate, w_up, w_down):
    return (F.silu(x @ w_gate) * (x @ w_up)) @ w_down
```

## 3. Stable Softmax
```python
def stable_softmax(x, dim=-1):
    z = x - x.max(dim=dim, keepdim=True).values
    e = z.exp()
    return e / e.sum(dim=dim, keepdim=True)
```

## 4. Top-p Sampling 核心
```python
def top_p_filter(logits, p=0.9):
    sorted_logits, idx = logits.sort(descending=True)
    probs = sorted_logits.softmax(-1)
    cdf = probs.cumsum(-1)
    remove = cdf > p
    remove[..., 1:] = remove[..., :-1].clone()
    remove[..., 0] = False
    sorted_logits[remove] = float('-inf')
    out = logits.new_full(logits.shape, float('-inf'))
    return out.scatter(-1, idx, sorted_logits)
```

## 5. Patchify
```python
def patchify(x, p):
    # [B,C,H,W] -> [B, N, C*p*p]
    B,C,H,W = x.shape
    assert H % p == 0 and W % p == 0
    x = x.reshape(B, C, H//p, p, W//p, p)
    x = x.permute(0,2,4,1,3,5)
    return x.reshape(B, (H//p)*(W//p), C*p*p)
```

## 6. GQA Head Mapping
```python
def repeat_kv(kv, n_q_heads, n_kv_heads):
    # kv [B,Hkv,L,d] -> [B,Hq,L,d]
    repeat = n_q_heads // n_kv_heads
    return kv.repeat_interleave(repeat, dim=1)
```
真实高性能实现不会简单复制所有 KV，但这段适合解释 head sharing。

## 7. Cross Entropy from Logits
```python
def ce_onehot(logits, target):
    logp = logits.log_softmax(-1)
    return -logp.gather(-1, target[..., None]).squeeze(-1).mean()
```

## 8. Cosine Similarity Matrix
```python
import torch.nn.functional as F

def cosine_matrix(a, b):
    a = F.normalize(a, dim=-1)
    b = F.normalize(b, dim=-1)
    return a @ b.T
```

## 9. Dice Score
```python
def dice(pred, gt, eps=1e-6):
    pred = pred.float().reshape(-1)
    gt = gt.float().reshape(-1)
    return (2*(pred*gt).sum()+eps)/(pred.sum()+gt.sum()+eps)
```

## 10. Simple Kalman / Hungarian 面试时要写到什么程度？
通常不要求从零实现完整 tracker。应能解释 state、prediction、cost matrix 和 assignment；若要求代码，可调用 `scipy.optimize.linear_sum_assignment` 后解释 complexity。

## 11. Gradient Norm
```python
def grad_norm(model):
    sq = 0.0
    for p in model.parameters():
        if p.grad is not None:
            sq += p.grad.detach().float().pow(2).sum().item()
    return sq ** 0.5
```

## 12. Parameter Count
```python
def n_params(model, trainable_only=False):
    ps = model.parameters()
    if trainable_only:
        ps = (p for p in ps if p.requires_grad)
    return sum(p.numel() for p in ps)
```

## 13. Visual-token Budget
```python
def total_visual_tokens(images, patch=14, merge=1):
    total = 0
    for h,w in images:
        n = (h//patch)*(w//patch)
        total += n // merge
    return total
```
真实模型应按 processor 的 resize/tile/merge 规则算。

## 14. Memory Estimate Checklist
面试不要求精确 allocator 行为，但要分：weights + gradients + optimizer + activations + attention/KV + temporary buffers。

## 15. Debug Wrapper
任何手写模块都建议先 assert：
```python
assert torch.isfinite(x).all()
assert x.dtype == expected_dtype
assert x.device == expected_device
assert x.shape[-1] == expected_hidden
```
