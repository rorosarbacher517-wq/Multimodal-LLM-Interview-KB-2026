# 02_KV_Cache怎么算

## 面试一句话

KV cache 大小近似与 batch × sequence length × layers × KV heads × head_dim × 2(K,V) × bytes 成正比。

## 核心回答

- GQA/MQA 通过减少 KV heads 降低 cache。
- 长上下文和大量视觉 token 会直接扩大 KV cache。
- 量化 KV cache 可以进一步降显存。

## 代码 / 公式

```python
def kv_cache_bytes(B, L, n_layers, n_kv_heads, head_dim, bytes_per_elem=2):
    return B * L * n_layers * n_kv_heads * head_dim * 2 * bytes_per_elem
```
