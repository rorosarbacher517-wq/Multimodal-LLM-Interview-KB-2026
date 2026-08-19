# 03_GUI_Agent怎么工作

## 面试一句话

GUI Agent 把屏幕理解转成动作序列，核心链路是 screenshot → grounding → action → new screenshot。

## 核心回答

- 动作包括 click(x,y)、type(text)、scroll、key press。
- 需要 UI 元素定位、OCR、状态变化识别。
- 训练可来自人工轨迹、自动探索、synthetic trajectory。
- 评测最终应看 task success，不只看 next-action accuracy。
