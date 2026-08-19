# 3D Perception 如何接 MLLM / VLA / World Model

## 面试一句话

MLLM 负责语义和推理，3D perception 提供 metric geometry、camera pose、object state 和 free space；VLA 需要两者共同完成可执行空间决策。

## 三种连接方式

### 1. Structured tool

```text
camera → depth/3D detector → JSON scene state → MLLM planner
```

### 2. 3D tokens

point/voxel/BEV features → projector → LLM/VLA token space。

### 3. Unified spatial foundation

直接用多视图/视频预训练得到 geometry-aware representations，再和 language/action 对齐。

## 为什么不能只靠 VLM 描述

“杯子在桌上”不等于知道杯子距机械臂 43 cm、抓取方向和碰撞空间。

## 面试关键词

metric depth、coordinate frame、camera pose、BEV、occupancy、3D tokens、spatial reasoning、closed-loop action。