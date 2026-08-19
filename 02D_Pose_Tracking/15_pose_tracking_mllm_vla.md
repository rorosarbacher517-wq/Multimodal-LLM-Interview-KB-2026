# Pose / Tracking 为什么对 MLLM 和 VLA 重要

## 面试一句话

MLLM 能描述“有人在走”，但机器人需要知道 **人在哪、手在哪里、目标怎么运动、下一帧会到哪里**；这些是 pose/tracking 提供的显式空间状态。

## 常见结合方式

```text
camera
→ detector / pose / tracker
→ structured state
→ MLLM / planner
→ action
```

也可以把 tracker 作为 tool，由 agent 在需要时调用。

## 场景

- GUI/video agent：持续绑定同一对象；
- robotics：hand/object trajectory；
- sports：pose + temporal action；
- safety：行人 trajectory prediction。

## 核心观点

语言 reasoning 不能替代稳定的几何测量。