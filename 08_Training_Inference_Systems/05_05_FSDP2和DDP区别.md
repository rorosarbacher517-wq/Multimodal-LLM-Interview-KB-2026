# 05_FSDP2和DDP区别

## 面试一句话

DDP 每张卡持有完整模型副本；FSDP2 把参数、梯度和优化器状态分片。

## 核心回答

- DDP：通信主要是 gradient all-reduce。
- FSDP2：forward/backward 前按需 all-gather 参数，之后重新释放/分片。
- FSDP2 基于 DTensor/per-parameter sharding，适合大模型。
- 多模态模型可对 vision tower、LLM 分别制定 sharding 策略。

## 参考

- https://docs.pytorch.org/docs/main/distributed.fsdp.fully_shard.html
