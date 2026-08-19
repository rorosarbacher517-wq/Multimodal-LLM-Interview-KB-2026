# BoT-SORT / OC-SORT：遮挡和相机运动怎么处理

## BoT-SORT

在 tracking-by-detection 基础上结合：

- motion model；
- appearance/ReID；
- camera motion compensation；
- 更稳健的 association。

适合相机本身移动的场景。

## OC-SORT

强调 observation-centric update。标准 Kalman 在长遮挡期间可能不断积累预测误差；OC-SORT 用真实 observation 重新修正轨迹，提升非线性运动和遮挡下的鲁棒性。

## 2026

OC-SORT 官方仓库在 2026 仍有实现加速更新。

## References

- BoT-SORT: https://github.com/NirAharon/BoT-SORT
- OC-SORT: https://github.com/noahcao/OC_SORT