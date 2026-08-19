# Document AI 怎么评测和诊断错误

## 面试一句话

文档解析不能只看一个总分，要把错误拆成 **detection、recognition、structure、reading order、serialization**。

## 常见指标

- OCR：CER / WER / normalized edit distance
- Detection：Precision / Recall / Hmean / IoU
- Table：structure similarity / cell matching
- Layout：mAP / region F1
- Parsing：element-level matching + edit/structure metrics
- QA：answer accuracy / exact match

## Bad Case 分类

1. 小字/模糊：perception；
2. 漏区域：layout detection；
3. 表格结构错：structure；
4. 多栏顺序错：reading order；
5. Markdown 标签错：serialization。

## 面试建议

先定位错误属于哪一层，再决定是加数据、升分辨率、换 detector 还是改后处理。