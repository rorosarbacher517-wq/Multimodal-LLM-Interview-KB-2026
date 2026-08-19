# 03B · Multimodal Generation & World Models

> 当前多模态岗位已经不只问“图片怎么进 LLM”，还会问 **文本/图像/视频怎么生成、理解与生成如何统一、world model 如何预测未来**。
>
> 建议在 `03 Multimodal Core Architecture` 后学习。

---

## Part A. Generative Modeling 基础

### Q1. Discriminative Model 和 Generative Model 区别？
- Discriminative：直接学 `p(y|x)` 或 decision boundary。
- Generative：学习数据分布/生成过程，目标是产生新的 `x` 或多模态输出。

MLLM understanding 偏 discriminative/generative language modeling；image/video generation 则直接建模视觉数据分布。

### Q2. 图像生成为什么比文本生成难直接做 Autoregressive？
像素数量巨大，例如 `1024×1024×3`。逐像素生成序列过长，因此通常先：
- 压到 latent；
- 离散 image tokens；
- 或用 diffusion/flow 在连续 latent 上生成。

### Q3. Continuous Latent 和 Discrete Token 有什么区别？
- continuous latent：实数向量，适合 diffusion/flow。
- discrete token：codebook index，可像文本一样 autoregressive 建模。

统一理解+生成模型经常需要在两类表示之间做设计选择。

---

## Part B. VAE / VQ-VAE / Image Tokenizer

### Q4. Autoencoder 在做什么？

```text
image → encoder → latent → decoder → reconstructed image
```

目标是用更紧凑 latent 保留主要信息。

### Q5. VAE 为什么有 KL Term？
VAE 不只重建，还约束 latent posterior 接近简单 prior，常见标准高斯：

```text
L = reconstruction + β KL(q(z|x) || p(z))
```

这样 latent space 更平滑、可采样。

### Q6. VQ-VAE 为什么把 latent 离散化？
Encoder 输出向量后，映射到最近 codebook vector，用离散 index 表示视觉内容。

这样可以把 image generation 转成 token modeling。

### Q7. 一个 Image Tokenizer 好不好看什么？
- reconstruction quality；
- compression ratio；
- codebook utilization；
- semantic consistency；
- tokenizer latency。

压缩太强会丢小字和纹理，太弱则 token 太多。

---

## Part C. Diffusion

### Q8. Diffusion Model 的核心直觉？
训练时逐步给数据加噪，模型学习如何去噪；推理从噪声开始多步反向还原出样本。

```text
x0 → noise → x_t
             ↓ model predicts denoising direction
noise → ... → generated x0
```

### Q9. Forward Diffusion 为什么通常不需要学习？
加噪过程由固定 noise schedule 定义，可以直接采样；真正学习的是 reverse denoising model。

### Q10. 模型预测 `ε`、`x0`、`v` 有什么区别？
它们是不同 parameterization：
- noise prediction；
- clean sample prediction；
- velocity-like combination。

本质都在学习反向生成方向，但训练稳定性和不同 noise level 权重会不同。

### Q11. DDPM 和 DDIM 区别怎么讲？
DDPM 是经典 stochastic reverse process；DDIM 构造了可用更少步、可更确定性采样的路径。

面试重点：**sampling step 数直接影响生成 latency**。

### Q12. Classifier-Free Guidance (CFG) 是什么？
同时计算 conditional 和 unconditional prediction，通过 guidance scale 放大条件方向。

过小：条件控制弱；过大：可能降低多样性、产生 artifact。

### Q13. Latent Diffusion 为什么重要？
不是在原始像素空间做 diffusion，而是在 VAE latent 空间生成：

```text
image → VAE latent
          ↓ diffusion
       new latent
          ↓ decoder
        image
```

大幅降低空间计算量。

---

## Part D. U-Net / DiT / MMDiT

### Q14. 为什么早期 Diffusion 常用 U-Net？
U-Net 具有多尺度 encoder-decoder + skip connections，能同时处理全局结构和局部细节。

### Q15. DiT 是什么？
Diffusion Transformer 用 Transformer 代替 U-Net backbone，对 latent patches 做 Transformer modeling。

它把生成模型带入更容易随参数/数据 scale 的 Transformer 路线。

### Q16. Text Condition 如何进入生成网络？
常见方式：
- cross-attention；
- adaptive normalization；
- joint token sequence。

文本 embedding 不是简单和每个像素 concat。

### Q17. MMDiT 为什么适合多模态生成？
Multimodal Diffusion Transformer 让 text/image latent 通过更深的 joint attention/双流交互参与生成，而不只是一个固定 text conditioning vector。

具体实现因模型而异，面试先掌握“多模态条件在 Transformer 内联合交互”的抽象。

---

## Part E. Flow Matching / Rectified Flow

### Q18. Flow Matching 和 Diffusion 的共同点？
都学习从简单分布（如 noise）到数据分布的变换路径。

区别在于 flow matching 更直接学习连续时间 vector field。

### Q19. Rectified Flow 的直觉？
希望学习更“直”的 transport trajectory，让 sampling 可以用较少 ODE steps 完成。

不要简单说“Flow 一定比 Diffusion 快”；速度仍取决于模型、solver 和步数。

### Q20. 为什么 2025–2026 越来越多生成模型讨论 Flow？
因为它适合 Transformer-based continuous generative modeling，并有机会在 sample quality 与 inference steps 间取得更好折中。

---

## Part F. Autoregressive / Masked Image Generation

### Q21. Autoregressive Image Token Generation 怎么做？

```text
image → discrete tokenizer → [z1,z2,...,zN]
model: p(z_t | z_<t, text)
```

优点是与 LLM 形式统一；缺点是长视觉 token sequence 解码慢。

### Q22. Masked Generative Modeling 和 AR 区别？
不是严格从左到右，而是反复预测一批 masked tokens，可以并行更新多个位置。

### Q23. 统一理解和生成最大的冲突是什么？
- understanding 需要抽象、语义、判别性强的特征；
- generation 需要保留足够视觉细节用于重建。

因此有的模型共享 backbone，有的像 Janus 一样解耦视觉表示路径。

---

## Part G. Unified Multimodal Models

### Q24. “统一模型”是不是所有模态都必须用一个 Encoder？
不是。统一可以发生在：
- shared LLM/Transformer；
- shared token space；
- shared training objective/interface。

不同模态仍可使用专门 encoder/decoder。

### Q25. InternVL-U 为什么值得 2026 面试关注？
InternVL-U 是公开的统一多模态路线案例：一个约 4B 模型同时覆盖理解、推理、图像生成和编辑，并把 MLLM 与 MMDiT-style generation head 结合。

面试重点是理解**统一理解与生成的接口设计**，而不是背 benchmark。

Primary source: https://arxiv.org/abs/2603.09877

### Q26. Image Editing 和 Text-to-Image 有什么额外输入？
Editing 还需要 source image，以及希望保留/改变哪些区域或属性。

常见任务：
- inpainting；
- object replacement；
- style/content edit；
- instruction-based editing。

评测必须同时看 instruction following 和 identity/content preservation。

---

## Part H. Video Generation / World Models

### Q27. Video Generation 比 Image Generation 多了什么难点？
- temporal consistency；
- object identity persistence；
- motion physics；
- camera motion；
- token/latent 数量大得多。

### Q28. 为什么只逐帧生成容易闪烁？
各帧独立时，没有机制约束同一对象在时间上连续，因此纹理、位置、形状会漂移。

### Q29. World Model 是什么？
模型根据当前状态和 action，预测未来状态/观察：

```text
state_t + action_t → predicted state_{t+1:T}
```

它可以用于 planning、robotics、autonomous agent、simulation。

### Q30. World Model 和普通 Video Generator 区别？
Video generator 重点是生成看起来合理的视频；world model 更强调**条件于 action/状态，未来变化要对决策有用**。

### Q31. VLA 与 World Model 如何结合？
- VLA：直接从 observation/instruction 预测 action。
- World Model：先预测不同 action 的未来结果，再规划。

二者可以端到端结合，也可以作为 policy + predictive model 两个模块。

---

## Part I. Evaluation / Serving

### Q32. 图像生成为什么不能只看 FID？
FID 是分布级统计指标，不能完整反映：
- prompt adherence；
- OCR/text rendering；
- human preference；
- identity preservation；
- safety。

### Q33. 生成模型的成本主要在哪里？
- latent/token 数；
- denoising/sampling steps；
- Transformer/U-Net FLOPs；
- text/vision encoder；
- decoder/VAE；
- video temporal length。

### Q34. 面试比较 AR、Diffusion、Flow 应该怎么答？
按四点：
1. representation：discrete vs continuous；
2. training objective；
3. sampling process；
4. quality / latency / controllability trade-off。

## Primary references
- VQ-VAE: https://arxiv.org/abs/1711.00937
- DDPM: https://arxiv.org/abs/2006.11239
- DDIM: https://arxiv.org/abs/2010.02502
- Latent Diffusion: https://arxiv.org/abs/2112.10752
- DiT: https://arxiv.org/abs/2212.09748
- Flow Matching: https://arxiv.org/abs/2210.02747
- InternVL-U: https://arxiv.org/abs/2603.09877
