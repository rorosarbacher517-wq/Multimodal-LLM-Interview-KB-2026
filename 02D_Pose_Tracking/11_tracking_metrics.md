# MOTA / IDF1 / HOTA：Tracking 怎么评测

## MOTA

综合 FP、FN、ID switch，偏向 detection + tracking overall error。

## IDF1

关注身份匹配正确性，适合衡量 ID 是否持续稳定。

## HOTA

试图更平衡地衡量 detection accuracy 和 association accuracy。

## 为什么不能只看 MOTA

一个 detector 很强但频繁换 ID 的 tracker，MOTA 可能看起来还不错，但真实 identity tracking 很差。

## 面试建议

如果业务目标是“统计人流”，可能 detection 更重要；如果是“同一辆车跨帧持续跟踪”，association/ID 更关键。