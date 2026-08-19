# SAM2 / Grounded SAM2 如何做 Video Object Tracking

## SAM2

```text
prompt on frame t
→ object mask
→ memory encoder
→ memory bank
→ next-frame image features + memory attention
→ next mask
```

它维持的是 object mask memory，而不是简单对每帧重新运行 SAM。

## Grounded SAM2

可以先用文本开放集 detector（如 GroundingDINO）找到对象，再用 SAM2 在视频里持续传播 mask。

## 与 MOT 区别

- ByteTrack：box + identity，轻量实时；
- SAM2：mask-level object propagation，更精细但更贵；
- 具体选型看业务是否真的需要像素级轮廓。