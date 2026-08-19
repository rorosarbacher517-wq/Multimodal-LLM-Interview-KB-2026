# Single-Object Tracking (SOT) 与 MOT 区别

SOT 给第一帧一个目标 box/template，后续持续跟这个目标；MOT 每帧可能有多个目标，需要 detection + identity association。

经典 SOT 路线包括 Siamese matching，现代方法也会使用 Transformer，例如 template/search region 交互。

```text
frame1 target template
      +
current search image
→ matching / transformer
→ current target box
```

SOT 更关注单目标 robustness；MOT 更关注 ID switch、association 和多目标管理。
