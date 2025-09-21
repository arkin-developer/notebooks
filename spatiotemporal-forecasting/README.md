---
title: "NYC出租车时空流量预测模型"
description: "基于空间PatchTST的城市交通需求时空预测"
date: 2025-01-27
tags: ["时序预测", "PatchTST", "交通预测", "时空数据", "深度学习"]
categories: ["notebooks"]
---

{{< lead >}}
基于现代空间PatchTST（Patch Time Series Transformer）的NYC出租车时空流量预测模型，用于预测曼哈顿地区未来3小时的出租车流量分布，支持流入量和流出量的双通道预测。
{{< /lead >}}


## Jupyter Notebook预览
<iframe 
  src="https://nbviewer.org/github/arkin-developer/notebooks/blob/main/time-series-forecasting/NYC_Taxi_Spatial_Forecasting.ipynb"
  width="100%"
  height="600px"
  frameborder="0"
  style="border: 1px solid #e9ecef; border-radius: 8px; margin: 2rem 0;"
  allowfullscreen>
</iframe>



## 项目概述

> 说明：本项目基于真实的NYC出租车GPS轨迹数据，利用空间PatchTST深度学习模型，实现对城市交通需求时空分布的预测。模型能够根据过去6小时（12个时间步）的交通流量数据，预测未来3小时（6个时间步）的流量分布情况。

**目标**：构建一个现代化的时空序列预测模型，用于城市交通调度优化和需求预测。模型采用Transformer架构，具有参数高效、训练快速的特点，能够处理32×32栅格规模的时空数据。
**硬件建议**：支持Apple Silicon MPS或CUDA的设备（推荐4GB+内存）；
**软件建议**：Python 3.8+、PyTorch 2.0+、支持MPS或CUDA。

------

## ✅ 本教程包括

1. 环境配置与硬件检测
2. 真实空间时序数据集下载
3. 数据集展示与分析
4. 空间PatchTST神经网络构建
5. 数据集处理与训练准备
6. 模型训练与监控
7. 模型评估与可视化
8. 项目总结与展望


## 🔬 技术特点

- **现代架构**：采用2023年SOTA的PatchTST Transformer架构
- **参数高效**：~93K参数，比传统ConvLSTM减少81%
- **时空建模**：同时处理空间（32×32栅格）和时间（6小时→3小时）维度
- **真实数据**：基于NYC出租车GPS轨迹的真实交通数据
- **双通道预测**：同时预测流入量和流出量
- **跨平台支持**：支持Apple Silicon MPS、CUDA和CPU
- **业务导向**：面向实际交通调度和运营优化场景

## 📊 模型架构

- **输入**：`(batch_size, 12, 2, 32, 32)` - 过去6小时的双通道空间数据
- **输出**：`(batch_size, 6, 2, 32, 32)` - 未来3小时的预测
- **核心组件**：时间Patch嵌入 + 空间位置编码 + Transformer编码器
- **预测头**：多层感知机 + 输出投影层
- **特征维度**：d_model=64, n_heads=4, n_layers=2（轻量级配置）

## 🎯 应用场景

- 🚗 出租车司机导航优化
- 📊 城市交通调度系统
- 💰 动态定价策略制定
- 🏙️ 城市交通规划
- 📈 需求预测与运力配置
- 🚦 智能交通管理系统

---

*你可以从导航栏跳转到对应的 Jupyter Notebook 的云服务平台进行尝试，抑或是下载 Notebook文件到本地运行。*
