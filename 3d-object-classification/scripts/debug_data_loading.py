#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试脚本：验证ModelNet40数据加载和预处理功能
解决Notebook中cell执行顺序问题
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datasets import load_dataset
from collections import Counter

def load_modelnet40_dataset():
    """加载ModelNet40数据集"""
    print("正在从Hugging Face下载ModelNet40数据集...")
    
    # 使用jxie/modelnet40数据集
    dataset = load_dataset("jxie/modelnet40")
    
    print("数据集下载完成！")
    print(f"数据集结构: {dataset}")
    print(f"训练集大小: {len(dataset['train'])}")
    print(f"测试集大小: {len(dataset['test'])}")
    
    return dataset

def analyze_dataset_structure(dataset):
    """分析数据集结构"""
    print("\n=== 数据结构分析 ===")
    print(f"数据集分割: {list(dataset.keys())}")
    print(f"训练集: {len(dataset['train'])} 样本")
    print(f"测试集: {len(dataset['test'])} 样本")

    # 分析数据存储结构
    sample = dataset['train'][0]
    print(f"\n数据存储结构:")
    print(f"  字段: {list(sample.keys())}")

    # 分析每个字段的存储方式
    for key, value in sample.items():
        if hasattr(value, 'shape'):
            print(f"  {key}: 数组存储, shape {value.shape}")
        elif isinstance(value, (int, float)):
            print(f"  {key}: 数值存储, 值 {value}")
        elif isinstance(value, str):
            print(f"  {key}: 字符串存储, 长度 {len(value)}")
        elif isinstance(value, list):
            print(f"  {key}: 列表存储, 长度 {len(value)}")
            if len(value) > 0 and isinstance(value[0], list):
                print(f"    嵌套列表形状: {len(value)} x {len(value[0])}")
        else:
            print(f"  {key}: {type(value).__name__} 存储")

    return sample

def analyze_point_cloud_data(sample):
    """分析点云数据"""
    print("\n=== 点云数据存储分析 ===")
    
    # 查找点云数据字段
    points_key = None
    for key in sample.keys():
        if 'input' in key.lower() or 'point' in key.lower() or 'data' in key.lower():
            points_key = key
            break
    
    if points_key:
        points_data = sample[points_key]
        print(f"点云数据字段: {points_key}")
        print(f"  存储方式: 列表存储")
        print(f"  数据长度: {len(points_data)}")
        
        if len(points_data) > 0:
            print(f"  第一个点: {points_data[0]}")
            print(f"  点的维度: {len(points_data[0])}")
            
            # 转换为numpy数组进行分析
            points_array = np.array(points_data)
            print(f"  转换后形状: {points_array.shape}")
            print(f"  数据类型: {points_array.dtype}")
            print(f"  数据范围: [{points_array.min():.3f}, {points_array.max():.3f}]")
            return points_array
    
    print("未找到点云数据字段")
    return None

def preprocess_point_cloud(points, num_points=1024):
    """
    预处理点云数据
    Args:
        points: 原始点云数据 (N, 3)
        num_points: 目标点数
    Returns:
        处理后的点云数据
    """
    # 随机采样到固定点数
    if len(points) > num_points:
        indices = np.random.choice(len(points), num_points, replace=False)
        points = points[indices]
    elif len(points) < num_points:
        # 如果点数不足，随机重复采样
        indices = np.random.choice(len(points), num_points, replace=True)
        points = points[indices]
    
    # 归一化到单位球
    centroid = np.mean(points, axis=0)
    points = points - centroid
    max_dist = np.max(np.linalg.norm(points, axis=1))
    points = points / max_dist
    
    return points

def test_preprocessing(dataset):
    """测试数据预处理功能"""
    print("\n=== 测试数据预处理 ===")
    
    # 获取样本数据
    sample_data = dataset['train'][0]
    points_data = sample_data['inputs']
    
    # 转换为numpy数组
    points = np.array(points_data)
    print(f"原始点云形状: {points.shape}")
    print(f"标签: {sample_data['label']}")
    
    # 预处理
    processed_points = preprocess_point_cloud(points)
    print(f"预处理后点云形状: {processed_points.shape}")
    print(f"点云范围: [{processed_points.min():.3f}, {processed_points.max():.3f}]")
    
    return processed_points

def visualize_point_cloud_2d(points, title="2D Projection"):
    """使用Matplotlib可视化3D点云的2D投影"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    # XY平面投影
    ax.scatter(points[:, 0], points[:, 1], c=points[:, 2], 
               cmap='viridis', s=1, alpha=0.6)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()

def main():
    """主函数"""
    print("开始调试ModelNet40数据加载...")
    
    try:
        # 1. 加载数据集
        dataset = load_modelnet40_dataset()
        
        # 2. 分析数据结构
        sample = analyze_dataset_structure(dataset)
        
        # 3. 分析点云数据
        points = analyze_point_cloud_data(sample)
        
        # 4. 测试预处理
        if points is not None:
            processed_points = test_preprocessing(dataset)
            
            # 5. 可视化测试
            print("\n=== 生成可视化测试 ===")
            visualize_point_cloud_2d(processed_points, "测试点云可视化")
        
        print("\n✅ 调试完成！所有功能正常")
        
    except Exception as e:
        print(f"❌ 调试过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
