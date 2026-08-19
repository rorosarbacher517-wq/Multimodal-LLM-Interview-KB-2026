# Agent / Tool Use / Protocol / Evaluation — Primary References

> 只保留对 Agent 面试有可复用方法价值的论文、官方规范和官方文档。框架名字会变，但 Agent Loop、Tool Use、State、Planning、Verification、Protocol、Sandbox、Evaluation 这些概念更稳定。

## A. Agent Reasoning / Tool Use
- ReAct — https://arxiv.org/abs/2210.03629
- Toolformer — https://arxiv.org/abs/2302.04761
- Reflexion — https://arxiv.org/abs/2303.11366
- Tree of Thoughts — https://arxiv.org/abs/2305.10601

## B. Protocols
- Model Context Protocol — https://modelcontextprotocol.io/
- MCP 2026-07-28 specification update — https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Google Agent2Agent (A2A) announcement — https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- Google 2026 guide to agent protocols — https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/

## C. Agent Runtime / Sandbox / Durable Execution
- OpenAI Agents SDK 2026 harness + sandbox update — https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- OpenAI tools for building agents — https://openai.com/index/new-tools-for-building-agents/

## D. Web / Computer-Use Evaluation
- WebArena — https://arxiv.org/abs/2307.13854
- BrowserGym — https://arxiv.org/abs/2412.05467
- OSWorld — https://arxiv.org/abs/2404.07972
- OSWorld 2.0 — https://arxiv.org/abs/2606.29537

## E. Coding Agents
- SWE-agent — https://arxiv.org/abs/2405.15793
- SWE-bench — https://arxiv.org/abs/2310.06770

## F. Evaluation Principle
Agent 论文/系统结果优先看：
1. environment 是否可执行；
2. task success 是否由环境状态验证；
3. 最大步数/工具预算；
4. model / prompt / tool setup；
5. 是否允许 retry / reflection / parallel tool calls；
6. token / latency / cost；
7. safety / invalid action；
8. benchmark contamination / environment drift。

不要只比较 leaderboard 单个百分比。
