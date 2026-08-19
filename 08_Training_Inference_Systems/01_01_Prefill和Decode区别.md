# 01_Prefill和Decode区别

## 面试一句话

Prefill 一次处理整段输入，计算密集；Decode 每步生成一个 token，通常更受内存带宽和 KV cache 影响。

## 核心回答

- 多模态请求的视觉 token 会显著增加 prefill。
- Decode 阶段每一步都读取历史 KV。
- 优化方向：prefill 看 attention/kernel/并行；decode 看 KV cache、batching、quantization。
