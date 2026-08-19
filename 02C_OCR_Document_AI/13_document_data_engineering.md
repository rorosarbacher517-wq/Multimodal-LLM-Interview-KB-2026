# OCR / Document 数据怎么生产和清洗

## 面试一句话

Document AI 数据质量需要同时保证 **文字正确、坐标正确、结构正确、阅读顺序正确**。

## 数据来源

- scanned PDF / born-digital PDF
- webpages / office documents
- synthetic documents
- invoices / receipts / forms
- academic papers / books

## 生产链

```text
raw file
→ render page
→ PDF parser / OCR teacher / layout teacher
→ element labels
→ cross-model verification
→ hard-case human review
→ train
→ bad-case mining
```

## 去重

既要做文件 hash / page image perceptual hash，也要检查文本 near-duplicate，防止 benchmark contamination。

## 数据增强

scan noise、rotation、perspective、blur、illumination、screen photo、compression，但要保证 label transformation 同步。