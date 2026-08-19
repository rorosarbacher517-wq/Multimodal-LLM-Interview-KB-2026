# 05 Advanced · Multimodal Data Infrastructure & Quality

> 补充大规模数据生产的工程细节：格式、sharding、去重、版权/隐私、采样、active learning、lineage。

### Q1. WebDataset / Parquet / Record Format 为什么重要？
十亿级样本不能靠“一个图片一个小文件”随便读。需要考虑：
- sequential I/O；
- compression；
- metadata schema；
- distributed sharding；
- streaming training。

### Q2. 为什么要 Shard？
把大量小文件打成较大的 shard，可以减少 metadata/file-open 开销，也方便多 worker/rank 分片读取。

### Q3. Shard 太大或太小分别有什么问题？
- 太小：文件系统压力大。
- 太大：随机访问、失败恢复和重新生成成本高。

需要按存储、网络、样本大小和训练 worker 数平衡。

### Q4. Streaming Dataset 和 Map-style Dataset 区别？
Map-style 能按 index 随机访问；streaming 更适合超大远程数据，但 shuffle、resume、exact epoch 定义更复杂。

### Q5. Data Loader 如何保证不同 Rank 不重复读？
需要 rank-aware shard assignment / distributed sampler，并在 resume 时保存 data cursor 或可重建的随机状态。

### Q6. MinHash / LSH 在文本去重里为什么有用？
MinHash 近似 Jaccard similarity；LSH 把相似样本高概率放入相同 bucket，避免所有样本两两比较。

### Q7. 图像近重复为什么不能只用 MD5？
resize、crop、重新编码后 bytes 已不同。需要 perceptual hash、image embedding 或局部 feature 近邻。

### Q8. 跨模态 Pair 去重怎么做？
同图不同 caption、同 caption 不同图都可能出现。应联合 image identity、text similarity、source URL 和 pair-level metadata 去重。

### Q9. 数据质量分数能否直接作为 Sampling Probability？
可以参考，但不能只采最高分。否则会损失 diversity/long-tail。实际常结合 quality、domain、difficulty、novelty 做分层采样。

### Q10. Temperature Sampling 是什么？
对不同 domain 的原始比例做幂次平滑：小 domain 被适当上采样，大 domain 被压平，防止数据量最大的桶完全支配训练。

### Q11. Hard-negative Mining 在多模态数据中怎么做？
找“语义很像但不是正确配对”的 image-text/region-text pair，训练模型学更精细的边界。

### Q12. Active Learning 的核心？
不随机标所有数据，而优先标：
- 高不确定；
- 模型分歧大；
- 覆盖新 cluster；
- 业务高价值 bad cases。

### Q13. Curriculum Data 和 Mixture Optimization 有什么区别？
- mixture：某阶段不同数据比例。
- curriculum：不同训练阶段的数据难度/类型随时间变化。

### Q14. 数据 Licensing 为什么是技术问题？
需要 sample-level source/license/provenance，否则后续无法：
- 删除指定来源；
- 做合规审计；
- 重新构建训练集。

### Q15. PII 清洗为何不能只扫文本？
还可能出现在图像身份证、车牌、人脸、音频声纹、PDF metadata 中。

### Q16. Data Lineage 至少记录什么？
```text
source_id
raw_hash
parser_version
filter_scores
filter_version
dedup_cluster
final_shard
mixture_version
```

### Q17. 训练后发现某批数据有问题怎么办？
必须能从 experiment → dataset version → shard → original source 反查，必要时重建不含该来源的新版本。

### Q18. 如何评价“一批新数据值不值得加”？
做 controlled small-scale experiments，看：
- target bucket gain；
- general capability regression；
- gain per token/GPU-hour；
- diversity overlap；
- bad-case coverage。
