# 07B · Multimodal Safety & Reliability

> 多模态 Agent 的风险不只来自文本 prompt。图片、PDF、网页、OCR、工具结果、音频和环境状态都可能携带不可信指令。
>
> 学习目标：**Threat Model → Input Trust → Model Policy → Tool Permission → Execution Sandbox → Evaluation → Monitoring**。

---

### Q1. Multimodal Safety 和普通 LLM Safety 最大区别？
攻击面更多：
- 图像中的文字；
- PDF/网页隐藏内容；
- OCR 结果；
- audio instruction；
- tool result；
- GUI state。

模型必须区分“用户指令”和“环境中不可信内容”。

### Q2. 什么是 Prompt Injection？
外部内容试图让模型忽略原任务、执行攻击者指令。

在 multimodal RAG/Agent 中，网页或图片本身就可能包含恶意 prompt。

### Q3. Direct Injection 和 Indirect Injection 区别？
- Direct：用户直接写攻击指令。
- Indirect：攻击指令藏在模型读取的文档、网页、图像、工具返回中。

Agent 场景最危险的通常是 indirect injection，因为模型会主动读取外部世界。

### Q4. OCR Injection 是什么？
图片/文档中的文字被 OCR/MLLM 读出后，内容可能被错误地当成 system/user instruction。

防御核心是**数据与指令分层**，而不是“让模型更聪明”。

### Q5. Adversarial Example 和 Prompt Injection 一样吗？
不一样。
- adversarial example：通过输入扰动改变模型预测。
- prompt injection：利用模型遵循自然语言指令的机制越权。

二者都属于 robustness/security，但威胁模型不同。

### Q6. RAG Poisoning 是什么？
知识库里被写入恶意或错误内容，retrieval 后影响回答或工具决策。

需要 source trust、document ACL、ingestion validation、citation/evidence check。

### Q7. 为什么 Function Calling 会放大安全风险？
纯聊天输出错了可能只是文字；tool call 可以真的：
- 发邮件；
- 删除文件；
- 修改数据库；
- 下单/支付；
- 控制设备。

所以必须把“模型建议”和“实际权限”分开。

### Q8. Least Privilege 是什么？
每个工具只给完成任务所需的最小权限。例如读取日历的 agent 不应默认拥有删除云盘文件权限。

### Q9. 为什么高风险 Action 需要 Confirmation？
因为 perception/reasoning 都可能错。对不可逆操作，在执行前展示：
- 要做什么；
- 影响对象；
- 关键参数；
- 请求用户确认。

### Q10. Sandbox 解决什么？
把代码/浏览器/文件操作限制在隔离环境中，降低错误或恶意 action 对真实系统的影响。

### Q11. Allowlist / Denylist 有什么用？
对 domain、tool、path、command、API operation 做可执行范围限制。它是 policy enforcement，不依赖模型自己记住规则。

### Q12. Multimodal Agent 为什么要做 Action Verification？
点击/工具执行后重新观察环境，确认结果是否符合预期：

```text
plan → act → observe → verify → continue/recover
```

### Q13. 什么是 Data Exfiltration 风险？
Agent 可能把私有 context、RAG 文档、tool result 发送到不应访问的外部目标。

需要信息流控制、tool ACL、日志和敏感数据检测。

### Q14. PII 在多模态里有哪些形式？
不只文本：
- 人脸；
- 身份证/车牌；
- 屏幕截图；
- 语音身份；
- 文档 metadata。

数据 pipeline 要在采集、训练和在线日志多个阶段治理。

### Q15. Safety Fine-tuning 能解决所有问题吗？
不能。模型 alignment 只是一个层。可靠系统还需要：
- input filtering；
- permissions；
- sandbox；
- output/tool validation；
- monitoring。

### Q16. Guard Model / Safety Classifier 放在哪里？
可以在：
- user input；
- retrieved content；
- model output；
- tool call；
- final action。

高风险业务通常需要多层 guardrails。

### Q17. Over-refusal 是什么？
模型为了安全，对本来允许且正常的请求也拒绝。Safety evaluation 要同时测：
- unsafe compliance；
- safe helpfulness。

### Q18. Multimodal Red Team 怎么设计？
覆盖：
- text-only attack；
- image embedded instruction；
- OCR obfuscation；
- malicious document；
- tool-result injection；
- multi-turn attack；
- GUI state manipulation。

### Q19. Agent Safety 为什么要测 End-to-End？
单步模型可能看起来安全，但多个 action 组合后可能产生危险结果。应评估最终 environment state 和 side effects。

### Q20. 线上应该记录什么 Audit Log？
至少：
- user request；
- model/tool versions；
- retrieved sources；
- tool call + args；
- permission result；
- action result；
- confirmation；
- safety decision。

同时要符合隐私和数据保留策略。

### Q21. 一个安全的 GUI Agent 执行链怎么画？

```text
Screenshot / DOM
→ perception
→ plan
→ policy check
→ permission check
→ optional confirmation
→ sandboxed action
→ new state
→ verifier
→ audit log
```

### Q22. 面试问“如何防 Prompt Injection”怎么答？
不要回答“写更强 system prompt”。完整答案：
1. untrusted content 标记；
2. instruction/data separation；
3. tool least privilege；
4. sensitive action confirmation；
5. sandbox；
6. output/action validation；
7. attack eval + monitoring。
