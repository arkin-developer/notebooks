---
title: "🦜 LLM应用开发篇 - LangChain全栈开发实战"
description: "掌握LangChain框架核心技能，构建智能RAG问答系统"
date: 2025-10-12
tags: ["LangChain", "RAG", "向量数据库", "Prompt Engineering", "Agent", "LLM应用开发"]
categories: ["notebooks"]
---

# 🦜 LangChain 全栈开发实战

## 📋 项目简介

本项目全面展示 LangChain 框架的核心开发技能，从基础的 Prompt Engineering 到高级的 RAG 系统构建，覆盖生产级 LLM 应用开发的完整技术栈。

## 🎯 技能覆盖

### 1. Prompt Engineering 技术
- ✅ Zero-shot Prompting
- ✅ Few-shot Prompting
- ✅ Chain of Thought (CoT)
- ✅ ReAct (Reasoning + Acting)
- ✅ Reflexion
- ✅ Prompt Chaining

### 2. LangChain 核心组件
- ✅ LLM & Chat Models
- ✅ PromptTemplates
- ✅ Output Parsers
- ✅ Chains (LCEL)
- ✅ Runnable 接口

### 3. 调试与监控
- ✅ Verbose 日志
- ✅ Debug 模式
- ✅ 自定义 Callback Handler
- ✅ LangSmith 集成准备

### 4. LangServe 服务化
- ✅ FastAPI 集成
- ✅ API 端点扩展
- ✅ 客户端调用示例

### 5. Chat History 对话历史
- ✅ 内存对话历史
- ✅ 文件持久化
- ✅ 带记忆的对话链
- ✅ 历史状态管理

### 6. 自定义 Tools & Agents
- ✅ 自定义 FunctionTool
- ✅ 同步/异步工具调用
- ✅ Agent 执行器
- ✅ 天气查询、网页搜索等实用工具

### 7. 向量数据库 & RAG
- ✅ Chroma 向量数据库
- ✅ Embeddings 向量化
- ✅ Similarity Search 相似度搜索
- ✅ RAG 增强检索
- ✅ 带记忆的 RAG 系统

### 8. Streamlit RAG 问答机器人
- ✅ Web 界面开发
- ✅ 对话历史可视化
- ✅ 来源文档展示
- ✅ 实时交互问答

## 📂 项目结构

```
langchain-development/
├── langchain-development.ipynb    # 主 Notebook
├── README.md                       # 项目文档
├── scripts/                        # 扩展脚本
│   ├── langserve_app.py           # LangServe API 服务
│   └── streamlit_app.py           # Streamlit Web 应用
├── chroma_db/                      # 向量数据库存储
└── chat_history.json              # 对话历史持久化
```

## 🚀 快速开始

### 安装依赖

```bash
pip install langchain langchain-openai langchain-community
pip install chromadb tiktoken
pip install langserve fastapi uvicorn
pip install streamlit
pip install requests beautifulsoup4
```

### 配置 DeepSeek API Key

本项目使用 **DeepSeek** 模型（兼容 OpenAI API，更便宜！）

```python
import os
os.environ["OPENAI_API_KEY"] = "your-deepseek-api-key-here"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"
```

**获取 API Key：**
1. 访问 [https://platform.deepseek.com/](https://platform.deepseek.com/)
2. 注册并创建 API Key
3. 替换上面代码中的 `your-deepseek-api-key-here`

**为什么选择 DeepSeek？**
- 💰 价格远低于 OpenAI（约 1/10 价格）
- 🚀 性能优秀，支持中文
- 🔌 完全兼容 OpenAI API 格式

### 运行 Notebook

```bash
jupyter notebook langchain-development.ipynb
```

### 启动 API 服务

```bash
cd scripts
python langserve_app.py
```

访问: http://localhost:8000/docs

### 启动 Web 应用

```bash
streamlit run scripts/streamlit_app.py
```

## 📊 核心内容

### 一、Prompt Engineering 技术

展示各种提示工程技术的实际应用，包括：
- 直接提示（Zero-shot）
- 示例学习（Few-shot）
- 思维链（CoT）
- 推理行动（ReAct）
- 提示链（Prompt Chaining）

### 二、LangChain 核心组件

深入理解和使用 LangChain 的核心抽象：
- 模型封装与调用
- 提示模板管理
- 输出解析器
- LCEL 表达式语言
- 链式组合

### 三、调试与监控

生产环境必备的调试和监控技术：
- Verbose 模式追踪
- Debug 详细日志
- 自定义回调处理
- 性能监控

### 四、对话历史管理

实现有状态的对话系统：
- 内存缓冲管理
- 文件持久化
- 会话状态维护
- 历史上下文感知

### 五、Tools & Agents

构建智能代理系统：
- 工具定义与注册
- 同步异步调用
- Agent 决策执行
- 多工具协同

### 六、向量数据库 & RAG

构建检索增强生成系统：
- 文档向量化
- 向量存储与检索
- 相似度匹配
- RAG 问答链
- 上下文增强

### 七、Web 应用开发

从 Demo 到生产：
- LangServe API 服务
- Streamlit 交互界面
- 客户端集成
- 部署方案

## 🎓 学习路径

1. **基础篇** (30分钟)
   - Prompt Engineering 技术
   - 核心组件使用

2. **进阶篇** (45分钟)
   - Tools & Agents
   - 向量数据库与检索

3. **实战篇** (60分钟)
   - RAG 系统构建
   - Web 应用开发

4. **生产篇** (30分钟)
   - 调试监控
   - 服务部署

## 💡 核心亮点

- 📝 **全面覆盖**: 涵盖 LangChain 所有核心技能点
- 🎯 **实战导向**: 每个技能都有可运行的代码示例
- 🔧 **生产就绪**: 包含调试、监控、部署等实用技术
- 🚀 **端到端**: 从概念到完整应用的闭环
- 📚 **代码简洁**: 清晰的代码结构，易于理解和扩展

## 🛠️ 技术栈

- **框架**: LangChain, LangServe
- **LLM**: DeepSeek Chat（兼容 OpenAI API）
- **向量数据库**: Chroma
- **Web框架**: FastAPI, Streamlit
- **工具库**: tiktoken, pydantic, beautifulsoup4

## 📈 扩展方向

- 🔄 **多模态支持**: 图像、音频处理
- ⚡ **流式输出**: 实时响应优化
- 🎯 **高级 RAG**: 重排序、混合检索、查询重写
- 🌐 **多语言支持**: 国际化处理
- 📊 **监控面板**: LangSmith 深度集成
- 🔒 **安全增强**: 内容过滤、访问控制

## 🤝 最佳实践

- ✅ 使用 LCEL 构建可组合的链
- ✅ 合理使用 Verbose 和 Debug 进行调试
- ✅ 为生产环境配置适当的内存管理策略
- ✅ 使用向量数据库优化检索性能
- ✅ 实现错误处理和重试机制
- ✅ 监控 Token 使用和成本

## 📝 注意事项

- 需要有效的 DeepSeek API Key（比 OpenAI 便宜很多！）
- 注意 Token 使用量，但 DeepSeek 成本很低
- 向量数据库需要足够的磁盘空间
- 生产环境建议使用更 robust 的持久化方案

## 💡 DeepSeek vs OpenAI

| 特性 | DeepSeek | OpenAI |
|------|----------|---------|
| **价格** | ¥0.001/千tokens | ¥0.012/千tokens |
| **中文支持** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **API 兼容** | ✅ 完全兼容 | ✅ 原生支持 |
| **性能** | 接近 GPT-3.5 | GPT-3.5 |
| **注册** | 国内手机号 | 需要外区号码 |

**推荐使用 DeepSeek 的场景：**
- ✅ 学习和开发测试
- ✅ 中文为主的应用
- ✅ 预算有限的项目
- ✅ 国内部署的应用

## 📖 参考资源

- [LangChain 官方文档](https://python.langchain.com/)
- [DeepSeek 平台](https://platform.deepseek.com/) ⭐ 推荐
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs/)
- [OpenAI API 文档](https://platform.openai.com/docs)
- [Chroma 文档](https://docs.trychroma.com/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [Streamlit 文档](https://docs.streamlit.io/)

---

**作者**: Arkin  
**日期**: 2025-10-12  
**版本**: 1.0.0

