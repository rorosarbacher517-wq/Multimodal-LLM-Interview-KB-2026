# 多模态大模型为什么还需要 YOLO / SAM / GroundingDINO？

## 面试一句话

MLLM 擅长开放语义理解、推理和规划，但专用 perception models 在高分辨率定位、像素分割、实时延迟上往往更强，因此 2026 的 Agent 更像是**模型协作系统**。

## 一个典型分工

```text
MLLM
  ↓ 决定“我要找什么”
GroundingDINO / YOLOE
  ↓ boxes
SAM 2
  ↓ masks / tracking
MLLM
  ↓ 读取结构化结果并继续 reasoning / action
```

## 怎么选？

- **固定类别 + 实时部署**：YOLO11 / YOLO26 / RT-DETR。
- **类别会变化 + 文本 prompt**：GroundingDINO / YOLOE。
- **像素级 mask**：SAM / SAM 2。
- **长视频对象传播**：SAM 2 + 关键帧 grounding。
- **GUI / robot / agent**：MLLM 负责 planning，专用模型负责可靠 perception tool。

## 面试加分点

不要把“foundation model”理解成“所有子任务都必须由一个网络独立完成”。真实系统更看重**准确率、延迟、可控性和成本**。
