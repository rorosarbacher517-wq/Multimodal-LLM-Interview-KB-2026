# Tracking 工程化：Detector、Tracker、Latency 怎么配

## 面试一句话

Tracking 系统的延迟通常由 detector 主导，因此首先优化 detector frequency、resolution 和 batch，而不是只改 association 算法。

## 常见设计

### 每帧 detector
精度稳定，成本高。

### 间隔检测 + tracker propagation
例如每 N 帧重新检测，中间用 motion/point tracker。

### 多级模型
轻 detector 常跑；低置信或复杂帧调用大模型。

## 线上关注

- FPS / end-to-end latency；
- ID switch；
- lost track duration；
- memory growth；
- camera motion；
- detector domain shift。

## Debug 顺序

先确认是 detector 漏检、association 错配，还是 motion model 失效。