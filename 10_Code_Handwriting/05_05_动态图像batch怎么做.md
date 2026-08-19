# 05_动态图像batch怎么做

## 面试一句话

动态分辨率会导致每张图 visual token 数不同，因此不能直接普通 stack。

## 核心回答

- 方案一：padding + attention mask。
- 方案二：pack/flatten 多图 token，记录 offsets。
- 方案三：按视觉 token 长度 bucket，减少 padding。
- 训练框架还需要按 token budget 而不是仅 sample count 控 batch。
