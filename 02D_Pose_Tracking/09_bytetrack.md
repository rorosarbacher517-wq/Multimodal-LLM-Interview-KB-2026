# ByteTrack：为什么低分框也要用

## 面试一句话

ByteTrack 的核心不是更复杂的 ReID，而是 **不要过早丢掉低置信度 detection**；遮挡目标常常只是 score 低，并不是真的不存在。

## Association

1. 先用高分 detections 和 tracks 匹配；
2. 对没匹配上的 tracks，再与低分 detections 匹配；
3. 低分背景框因为无法与已有轨迹保持一致，通常不会长期存活。

## 为什么有效

传统 threshold 会直接删掉被遮挡目标，导致 trajectory fragmentation。ByteTrack 利用已有 track 的运动一致性恢复这些对象。

## Reference

- https://github.com/FoundationVision/ByteTrack
- https://arxiv.org/abs/2110.06864