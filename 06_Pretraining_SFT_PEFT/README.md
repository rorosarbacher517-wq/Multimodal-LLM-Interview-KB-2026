# 06 · Multimodal Pretraining, SFT & PEFT

## Q1. 一个 MLLM 通常分几阶段训练？

常见但非唯一的路线：

1. vision-language alignment；
2. large-scale multimodal pretraining / continued pretraining；
3. multimodal SFT；
4. preference optimization / RL；
5. agent/tool/domain specialization。

不同模型可能合并阶段，不能把 LLaVA 的 recipe 当成所有 VLM 的固定模板。

## Q2. 为什么早期 alignment 常冻结 Vision Encoder 和 LLM？

随机初始化 projector 时，直接全量训练可能破坏成熟 backbone。先只训练 connector，相当于先学会“把视觉语言翻译成 LLM 能理解的表示”。

随后再逐步解冻，学习更深的跨模态适配。

## Q3. Vision Encoder 到底要不要冻结？

取决于：

- 数据量；
- 视觉域是否和预训练差很多；
- OCR/grounding 是否需要改变底层视觉；
- GPU 预算；
- forgetting 风险。

医学、遥感、工业等视觉域偏移大时，更可能需要 vision-side tuning。

## Q4. Multimodal pretraining 和 SFT 的区别？

- Pretraining：学习广覆盖世界知识、视觉语言对齐和基础预测能力；数据规模大、格式弱约束。
- SFT：学习用户指令、回答格式、任务范式和对话行为；数据质量更重要。

SFT 不能替代预训练提供的大规模 perception/knowledge coverage。

## Q5. MLLM 的基础 language loss 怎么算？

最常见仍然是 next-token cross entropy：

```text
L = - Σ_t log p(y_t | context, y_<t)
```

图像没有必要单独有 pixel loss。视觉 encoder/projector 可以通过“答案 token 是否预测正确”收到梯度。

## Q6. 为什么 SFT 常只对 assistant tokens 计 loss？

system/user prompt 和 image placeholder 是条件，不是希望模型模仿生成的目标。

实现上 labels：

- assistant positions = token id；
- user/system/image positions = `-100`；
- CrossEntropyLoss ignore `-100`。

## Q7. 多模态 SFT batch 比文本 SFT 难在哪里？

每个样本的视觉 token 数差异巨大：

- 图片数量不同；
- 分辨率不同；
- 视频帧数不同。

如果只按 sample count 组 batch，容易突然 OOM。更合理的是按 **total token / visual token budget** 做 bucket/packing。

## Q8. LoRA 的原理是什么？

冻结原权重 `W`，只学习低秩增量：

```text
W' = W + BA
A ∈ R^{r×d_in}
B ∈ R^{d_out×r}
```

`r << d`，显著减少可训练参数和 optimizer state。

## Q9. LoRA 为什么常初始化成一边随机、一边 0？

让初始 `BA = 0`，因此模型一开始等价于原模型；另一边随机保证训练时可以产生非零梯度并逐渐学习更新。

不是“两个矩阵都全 0”，否则会出现对称/梯度问题。

## Q10. MLLM 的 LoRA 应该加在哪里？

- LLM attention/FFN：最常见；
- projector：视觉语言接口变化明显时；
- vision encoder：视觉域偏移大时；
- 全部一起：效果可能更强，但显存和 forgetting 风险更高。

选择要由领域差异和数据量决定。

## Q11. QLoRA 为什么省显存？

基座权重量化（常见 4-bit 存储），反向只训练 LoRA adapter；因此不需要为全模型保存高精度 optimizer state。

但计算时仍会有反量化/高精度累加，且视觉塔量化支持要单独确认。

## Q12. Full Fine-tuning 和 LoRA 怎么选？

**LoRA 更适合：** 数据小、预算有限、多个领域 adapter、快速实验。

**Full FT 更适合：** 数据足够大、需要大幅改变能力分布、追求上限。

面试不要说 LoRA “一定几乎不掉点”；不同任务差异很大。

## Q13. SFT 后模型视觉能力下降有哪些原因？

- 文本-only 数据比例过高；
- 视觉数据分辨率/质量低；
- learning rate 太大破坏 alignment；
- 回答可凭语言 shortcut，不需要看图；
- 缺少 OCR/grounding 等 perception supervision；
- 数据重复和单一风格导致过拟合。

## Q14. 如何减轻 SFT catastrophic forgetting？

- 混入一部分 pretraining/general data；
- 较低 learning rate；
- 冻结/LoRA；
- 多任务 balanced sampling；
- regularization；
- 训练过程中持续跑 general capability eval。

## Q15. Instruction data 的格式为什么影响模型？

Chat template 决定：

- role token；
- system prompt；
- image placeholder；
- tool schema；
- reasoning/non-reasoning switch。

同一模型如果 template 错，会出现明显性能下降甚至无法正确识别图像位置。

## Q16. 为什么要做 curriculum？

从容易、清晰监督到复杂 reasoning/agent trajectory，可以降低优化难度。

示例：

```text
caption / recognition
→ VQA / OCR / grounding
→ multi-image / video
→ visual reasoning
→ GUI / tool use
```

但 curriculum 是否有效要用 controlled experiment 验证，不能当固定规律。

## Q17. 多任务训练如何处理任务冲突？

可从三个层面：

- data mixture：调整 sampling ratio；
- optimization：gradient clipping / task-aware weighting；
- architecture：adapter / expert / task-specific head。

最先做的一般是诊断 per-task loss 与 benchmark，而不是立刻设计复杂算法。

## Q18. 训练 MLLM 最重要的 ablation 有哪些？

至少控制：

- vision encoder；
- input resolution / visual tokens；
- connector；
- frozen vs unfrozen；
- data mixture；
- pretrain/SFT stage；
- RL/post-training；
- text-only retention。

一次只改一个关键因素，才能知道增益从哪里来。