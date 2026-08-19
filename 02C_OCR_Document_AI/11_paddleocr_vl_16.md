# PaddleOCR-VL-1.6：2026 文档解析路线

## 面试一句话

PaddleOCR-VL-1.6 的公开 pipeline 是 **layout analysis → element crop → VLM recognition → reading-order merge**，不是简单把整页 PDF 直接丢给一个 LLM。

## 两阶段流程

```text
Full page
→ PP-DocLayoutV3
→ element boxes / irregular regions + reading order
→ crop original-resolution elements
→ PaddleOCR-VL VLM
→ text / table / formula / chart results
→ merge
```

## 为什么合理

高分辨率整页直接进入 VLM 很贵。先做 layout，再在原始分辨率 crop 上识别，可以把计算集中到有信息的区域。

## 截至 2026-08

官方已发布 PaddleOCR-VL-1.6，VLM 仍为紧凑 0.9B 级，并强化 text、formula、table、chart、seal 等文档元素处理。

## Primary source

- https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md