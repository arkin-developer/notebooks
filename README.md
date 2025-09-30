# 深度学习实战项目集

> 涵盖 3D 视觉、时空预测、大语言模型微调的深度学习项目集合

---

## 项目列表

### 1. [3D 物体分类](./3d-object-classification/)

基于 PointMLP 的轻量级 3D 点云分类模型，在 ModelNet40 数据集上实现 84.5% 的准确率。

**核心技术**：
- FPS（最远点采样）算法保证空间均匀采样
- 多策略数据增强（旋转、缩放、抖动、点丢弃）
- 轻量级 MLP 架构（1.37M 参数）
- 端到端训练流程

**数据集**：ModelNet40（12,311 个 3D 模型，40 类物体）

---

### 2. [时空流量预测](./spatiotemporal-forecasting/)

基于 PatchTST Transformer 的 NYC 出租车时空需求预测模型，预测未来 3 小时的流量分布。

**核心技术**：
- PatchTST 时序预测架构
- 时空数据网格化处理（32×32 栅格）
- 参数高效设计（93K 参数）
- 双通道预测（上客量+下客量）

**数据集**：NYC 出租车 GPS 轨迹数据（2016 年 1 月）

---

### 3. [Qwen2.5 大语言模型微调](./qwen2.5-fine-tuning/)

基于 LoRA/QLoRA 的参数高效大模型微调案例，在单卡 A10 上完成指令微调。

**核心技术**：
- LoRA/QLoRA 参数高效微调
- ModelScope 模型下载与管理
- 指令微调完整流程
- 单卡训练优化

**模型**：Qwen2.5-1.5B-Instruct

---

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/arkin-developer/notebooks.git
cd notebooks

# 进入项目目录
cd 3d-object-classification  # 或其他项目

# 启动 Jupyter Notebook
jupyter notebook
```

每个项目目录下都有详细的 README 文档和完整的 Jupyter Notebook。

---

## 项目结构

```
notebooks/
├── 3d-object-classification/       # 3D 物体分类
├── spatiotemporal-forecasting/     # 时空流量预测
├── qwen2.5-fine-tuning/            # 大模型微调
└── README.md
```

---

## 环境要求

- Python 3.8+
- PyTorch 2.0+
- Jupyter Notebook
- 其他依赖见各项目的 README

---

*详细文档和使用说明请参考各项目目录下的 README 文件*
