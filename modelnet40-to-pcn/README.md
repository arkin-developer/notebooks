# ModelNet40 to PCN 数据集转换工具

这个项目将ModelNet40分类数据集转换为PCN风格的点云补全数据集，支持多种遮挡策略和数据增强方法。

## 项目概述

点云补全任务需要配对的数据集：每个样本包含一个不完整的点云和对应的完整点云。本项目通过从ModelNet40数据集生成人工遮挡的不完整点云，构造出类似PCN数据集的点云补全训练数据。

## 主要特性

- 🎯 **多遮挡策略**：支持随机、视角、距离、平面等多种遮挡方式
- 📊 **数据增强**：旋转、缩放、噪声等增强方法
- 🔧 **灵活配置**：可自定义遮挡比例、策略组合等参数
- 📈 **可视化支持**：直观展示遮挡效果和数据集统计
- 💾 **批量处理**：支持大规模数据集的批量转换

## 项目结构

```
modelnet40-to-pcn/
├── modelnet40-to-pcn.ipynb    # 主要演示notebook
├── README.md                  # 项目说明
└── scripts/                   # 核心代码模块
    ├── modelnet40_downloader.py    # ModelNet40数据下载
    ├── occlusion_strategies.py     # 遮挡策略实现
    ├── pcn_dataset.py              # PCN风格数据集类
    ├── data_augmentation.py        # 数据增强工具
    ├── visualization.py            # 可视化工具
    └── dataset_converter.py        # 数据集转换主程序
```

## 遮挡策略

### 1. 随机遮挡 (Random Occlusion)
- 随机移除指定比例的点
- 模拟传感器故障或数据丢失

### 2. 视角遮挡 (View Occlusion)
- 从特定视角移除点
- 模拟单视角扫描的局限性

### 3. 距离遮挡 (Distance Occlusion)
- 移除距离中心过远的点
- 模拟激光雷达的有效范围

### 4. 平面遮挡 (Plane Occlusion)
- 使用平面切割移除点
- 模拟墙或障碍物遮挡

### 5. 噪声遮挡 (Noise Occlusion)
- 添加噪声后移除异常点
- 模拟传感器噪声影响

## 快速开始

### 1. 环境要求
```bash
pip install torch torchvision numpy matplotlib scikit-learn tqdm
```

### 2. 运行演示
```bash
jupyter notebook modelnet40-to-pcn.ipynb
```

### 3. 命令行使用
```bash
python scripts/dataset_converter.py --input_dir ./modelnet40 --output_dir ./pcn_dataset
```

## 使用示例

```python
from scripts.pcn_dataset import ModelNet40ToPCNDataset
from scripts.occlusion_strategies import create_partial_pointcloud

# 创建PCN风格数据集
dataset = ModelNet40ToPCNDataset(
    modelnet_data=modelnet_data,
    strategies=['random', 'view', 'distance'],
    completion_ratio_range=(0.3, 0.7)
)

# 获取样本
sample = dataset[0]
partial_pc = sample['partial']    # 不完整点云
complete_pc = sample['complete']  # 完整点云
category = sample['category']     # 类别标签
```

## 配置选项

```python
config = {
    'strategies': ['random', 'view', 'distance', 'plane', 'noise'],
    'completion_ratio_range': [0.3, 0.7],
    'num_samples_per_model': 5,
    'data_augmentation': {
        'rotation': True,
        'scaling': True,
        'jittering': True
    }
}
```

## 数据集统计

转换后的数据集包含：
- **样本数量**：ModelNet40样本数 × 每模型生成样本数
- **点云密度**：2048点/样本（可配置）
- **遮挡比例**：30%-70%（可配置）
- **类别数量**：40个（继承自ModelNet40）

## 评估指标

- **Chamfer Distance (CD)**
- **Earth Mover's Distance (EMD)**
- **F1 Score**
- **Completion Quality**

## 扩展功能

- [ ] 支持更多遮挡策略
- [ ] 添加真实场景遮挡模拟
- [ ] 支持其他3D数据集转换
- [ ] 集成到现有点云补全框架

## 参考资料

- [ModelNet40 Dataset](https://modelnet.cs.princeton.edu/)
- [PCN: Point Completion Network](https://arxiv.org/abs/1808.00671)
- [PointNet: Deep Learning on Point Sets for 3D Classification](https://arxiv.org/abs/1612.00593)

## 许可证

MIT License
