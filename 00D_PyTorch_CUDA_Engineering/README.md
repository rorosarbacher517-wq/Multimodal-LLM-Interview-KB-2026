# 00D · PyTorch & CUDA Engineering Fundamentals

> 目标：补上“懂公式，但代码和 GPU 跑不明白”的断层。
>
> 建议在 `00B Deep Learning` 之后、`01 Transformer` 前并行学习。面试重点不是背 API，而是理解 **Tensor 如何存、梯度如何流、CPU/GPU 如何搬、kernel 为什么快/慢、OOM 怎么定位**。

---

## Part A. PyTorch Module 与 Tensor

### Q1. `Tensor`、`Parameter`、`nn.Module` 是什么关系？
- `Tensor`：数值数据。
- `nn.Parameter`：被注册为可训练参数的 Tensor。
- `nn.Module`：组织 parameters、buffers 和子模块的容器。

`model.parameters()` 只会返回注册好的 Parameter。

### Q2. 为什么直接把一个 Tensor 放到类属性里不一定被 optimizer 更新？
只有注册成 `nn.Parameter`，或者通过子 `nn.Module` 间接注册，optimizer 才会从 `model.parameters()` 找到它。

### Q3. Buffer 是什么？
不是 trainable parameter，但要随模型保存/迁移 device，例如 BatchNorm running statistics。

```python
self.register_buffer("mask", mask)
```

### Q4. `train()` 和 `eval()` 做了什么？
它们不会关闭梯度，而是切换某些模块行为，例如 Dropout、BatchNorm。

推理通常还要配合：

```python
with torch.inference_mode():
    ...
```

### Q5. `no_grad()`、`inference_mode()`、`detach()` 区别？
- `no_grad()`：上下文中不记录梯度图。
- `inference_mode()`：更激进的推理优化，适合纯 inference。
- `detach()`：返回与原 tensor 共享数据、但切断当前 autograd history 的 tensor。

---

## Part B. Autograd 与计算图

### Q6. Leaf Tensor 是什么？
通常用户创建且 `requires_grad=True` 的参数是 leaf。反向后 `.grad` 默认积累在 leaf tensor 上。

### Q7. 为什么 PyTorch 的 gradient 默认累加？
因为同一个参数可以被多条计算路径使用，也便于 gradient accumulation。

所以训练循环需要显式：

```python
optimizer.zero_grad()
```

### Q8. `retain_graph=True` 为什么不应随便用？
正常 backward 后计算图会释放。`retain_graph=True` 保留图，方便再次反传，但会占额外内存。

如果为了“修报错”到处打开它，常导致 OOM。

### Q9. In-place operation 为什么可能破坏 backward？
Autograd 可能需要 forward 的旧值计算梯度。原地修改后旧值消失，PyTorch 会报 version mismatch 或得到错误语义。

### Q10. Gradient Hook 有什么用？
可以查看/修改梯度，用于：
- debug 梯度是否为 0/NaN；
- gradient clipping/monitoring；
- distributed/optimizer 系统实现。

---

## Part C. Shape、Stride 与 Memory Layout

### Q11. `view()` 和 `reshape()` 区别？
`view()` 需要兼容当前 memory layout；`reshape()` 必要时会复制。

因此 `reshape()` 更方便，但可能隐藏一次 memory copy。

### Q12. 为什么 `transpose()` 后经常要 `.contiguous()`？
Transpose 往往只改变 stride，不实际重排内存。某些后续 `view()`/kernel 需要连续存储：

```python
x.transpose(1,2).contiguous().view(...)
```

### Q13. Contiguous 到底是什么意思？
Tensor 的逻辑索引顺序与底层线性内存布局匹配，stride 满足连续存储规则。

理解它对 attention reshape、image layout、kernel 性能都很重要。

### Q14. Broadcasting 为什么危险？
它能让 shape 不同的 tensor 自动扩展，代码很简洁；但如果维度含义错了，代码仍可能“能跑”。

多模态 bug 很多来自 `[B,L]`、`[B,1,L]`、`[B,H,L,L]` mask 的错误广播。

---

## Part D. Dataset / DataLoader

### Q15. `Dataset` 和 `DataLoader` 分别负责什么？
- Dataset：定义一个样本如何读取。
- DataLoader：batch、shuffle、多进程预取、collate。

### Q16. `collate_fn` 为什么对多模态特别重要？
图片尺寸、图片数、视频帧数和文本长度都可能不同，需要：
- padding；
- packing；
- dynamic resolution；
- metadata/offsets。

### Q17. `num_workers` 越大越好吗？
不是。过多 worker 会带来：
- CPU 争用；
- 内存复制；
- 文件系统压力；
- process startup 开销。

应该 profile data time 和 GPU idle time 后调。

### Q18. `pin_memory=True` 有什么意义？
Pinned host memory 可更高效地做 CPU→GPU DMA，配合 `non_blocking=True` 有机会让数据拷贝和计算重叠。

### Q19. 数据加载慢怎么排查？
依次看：
1. 文件 I/O；
2. image/video decode；
3. augmentation；
4. tokenizer；
5. worker；
6. CPU→GPU copy；
7. batch imbalance。

---

## Part E. Mixed Precision 与数值

### Q20. `autocast` 在做什么？
让适合低精度的算子使用 FP16/BF16，同时保留需要高精度的算子，减少显存并利用 Tensor Core。

### Q21. 为什么 BF16 通常不需要传统 Loss Scaling？
BF16 exponent range 接近 FP32，较不容易因为数值太小 underflow；FP16 exponent range 更窄，因此更常需要 loss scaling。

### Q22. Mixed Precision 为什么不代表所有 Tensor 都是低精度？
参数 master copy、optimizer state、部分 reduction/normalization 仍可能使用 FP32。具体取决于框架和训练配置。

---

## Part F. GPU / CUDA 基础

### Q23. GPU 为什么适合深度学习？
大量相似计算可以并行，尤其矩阵乘、卷积、attention 等高吞吐算子。

GPU 强项不是“单个核心更快”，而是**高并行吞吐 + 高带宽 + 专用矩阵单元**。

### Q24. GPU Memory Hierarchy 怎么粗略理解？
从大到小/慢到快可以粗略看：

```text
HBM/Global Memory
→ L2 Cache
→ Shared Memory / L1
→ Registers
```

高性能 kernel 很大一部分工作就是减少对 HBM 的重复读写。

### Q25. 什么是 Kernel Launch？
CPU 向 GPU 提交一个 kernel 执行。非常多极小 kernel 会被 launch overhead 拖慢，所以 fusion 很重要。

### Q26. Compute-bound 和 Memory-bound 怎么区分？
- Compute-bound：算术单元成为瓶颈。
- Memory-bound：数据搬运速度成为瓶颈。

大矩阵 prefill 更可能 compute-heavy；LLM 单 token decode 常更受权重/KV 读取影响。

### Q27. 什么是 Coalesced Memory Access？
相邻线程访问相邻内存，使 GPU 能合并 memory transaction，提升有效带宽。

### Q28. Tensor Core 在做什么？
专门加速低精度矩阵乘累加，例如 FP16/BF16/FP8 GEMM。维度对齐和 kernel 实现会影响能否充分利用。

### Q29. CUDA Stream 是什么？
一个有序执行队列。不同 stream 在依赖允许时可以重叠计算与数据传输。

大多数应用先用默认 stream；做高性能 pipeline 时再考虑显式 stream/event。

---

## Part G. Profiling / Compilation / OOM

### Q30. `torch.profiler` 应该看什么？
- CPU time；
- CUDA kernel time；
- memory；
- operator shape；
- communication；
- data loader gaps。

先找到 top bottleneck，再优化。

### Q31. `torch.compile` 的目标是什么？
捕获并优化计算图，做 graph-level optimization、operator fusion 和 backend code generation。

它不是“打开后所有模型必然更快”，动态 shape、多模态 control flow 和 unsupported ops 都可能影响收益。

### Q32. CUDA OOM 先看什么？
先区分：
- parameter/optimizer；
- activation；
- attention matrix；
- KV cache；
- temporary workspace；
- fragmentation。

然后打印最大 tensor shape 和峰值 memory。

### Q33. `memory_allocated` 和 `memory_reserved` 为什么不同？
PyTorch caching allocator 会预留显存块以便复用，所以 reserved 通常大于当前 tensor 真正 allocated 的内存。

### Q34. OOM 为什么可能是 Fragmentation？
总剩余显存看似够，但没有足够大的连续 block 满足新的 allocation。动态尺寸 workload 尤其容易出现。

### Q35. Activation Checkpointing 为什么有效？
少保存 forward activation，backward 时重算。它主要降低 activation memory，不会神奇减少参数/optimizer state。

---

## Part H. 分布式前置知识

### Q36. NCCL 是什么？
NVIDIA Collective Communications Library，为 GPU 间 all-reduce、all-gather、reduce-scatter、all-to-all 等 collective 提供高性能实现。

### Q37. 为什么网络拓扑会影响训练速度？
节点内 NVLink/NVSwitch 与节点间 InfiniBand/RDMA 带宽和延迟不同。

TP/EP 等高频通信最好尽量利用高带宽拓扑。

### Q38. PyTorch 多模态训练最常见的工程 bug？
- image placeholder 数与视觉 feature 不一致；
- attention mask/position id 长度没同步；
- variable-resolution batch padding 错；
- dtype/device 不一致；
- hidden size 不匹配；
- 某个超长视频拖垮整个 rank。

### Q39. 一个工程问题的推荐排查顺序？

**Reproduce → print shape/dtype/device → isolate smallest failing batch → profiler/memory snapshot → fix → regression test。**

不要一开始就随机改 batch size、learning rate 或 CUDA 环境。

## 推荐官方资料
- PyTorch docs: https://pytorch.org/docs/stable/
- PyTorch profiler: https://pytorch.org/docs/stable/profiler.html
- PyTorch compile: https://pytorch.org/docs/stable/torch.compiler.html
- CUDA Programming Guide: https://docs.nvidia.com/cuda/cuda-c-programming-guide/
