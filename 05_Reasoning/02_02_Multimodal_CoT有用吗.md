# 02_Multimodal_CoT有用吗

## 面试一句话

有用，但前提是 CoT 真的引用视觉证据；纯文本长思维链可能放大幻觉。

## 核心回答

- 对 geometry/chart/diagram 等多步任务更有效。
- 最好把 grounding、crop、OCR 或 timestamp 作为中间证据。
- 最终答案准确率之外，还应评估 reasoning faithfulness。
