# visualize_logs_simple.py - 最简单的版本
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

# 设置使用英文字体
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-darkgrid')

print("✅ Using English fonts for compatibility")
# ========== 配置结束 ==========

# 设置图表样式
plt.style.use('seaborn-v0_8-darkgrid')

def create_visualizations(df):
    """创建可视化图表"""
    print("🎨 开始生成可视化图表...")
    
    # 创建画布
    fig, axes = plt.subplots(2, 3, figsize=(16, 12))
    axes = axes.flatten()  # 将2x3的axes数组展平为1维
    
    # 1. IP访问频率柱状图
    ax = axes[0]
    ip_counts = df['ip_address'].value_counts()
    bars = ax.bar(range(len(ip_counts)), ip_counts.values, color='skyblue', edgecolor='black')
    ax.set_title('IP Address Access Frequency', fontsize=14, fontweight='bold')
    ax.set_xlabel('IP Rank')
    ax.set_ylabel('Access Count')
    ax.set_xticks(range(len(ip_counts)))
    ax.set_xticklabels(ip_counts.index, rotation=45)
    
    # 2. 响应码分布饼图
    ax = axes[1]
    response_counts = df['response_code'].value_counts()
    colors = ['#4CAF50', '#FF9800', '#F44336', '#2196F3', '#9C27B0']
    ax.pie(response_counts.values, labels=response_counts.index, autopct='%1.1f%%', 
           colors=colors, startangle=90)
    ax.set_title('HTTP Response Code Distribution', fontsize=14, fontweight='bold')
    
    # 3. 按小时访问趋势图（如果有时间数据）
    ax = axes[2]
    if 'timestamp' in df.columns:
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['hour'] = df['timestamp'].dt.hour
            hourly_counts = df.groupby('hour').size()
            ax.plot(hourly_counts.index, hourly_counts.values, marker='o', linewidth=2)
            ax.set_title('Access Trend by Hour', fontsize=14, fontweight='bold')
            ax.set_xlabel('Hour')
            ax.set_ylabel('Request Count')
            ax.grid(True, linestyle='--', alpha=0.5)
        except:
            ax.text(0.5, 0.5, '时间数据格式错误', ha='center', va='center')
            ax.set_title('按小时访问趋势', fontsize=14, fontweight='bold')
    else:
        ax.text(0.5, 0.5, '无时间戳数据', ha='center', va='center')
        ax.set_title('按小时访问趋势', fontsize=14, fontweight='bold')
    
    # 4. 各IP流量消耗水平条形图
    ax = axes[3]
    ip_traffic = df.groupby('ip_address')['bytes_sent'].sum().sort_values()
    if len(ip_traffic) > 0:
        bars = ax.barh(range(len(ip_traffic)), ip_traffic.values)
        ax.set_title('Traffic Consumption by IP', fontsize=14, fontweight='bold')
        ax.set_xlabel('Traffic (bytes)')
        ax.set_yticks(range(len(ip_traffic)))
        ax.set_yticklabels(ip_traffic.index)
    else:
        ax.text(0.5, 0.5, '无流量数据', ha='center', va='center')
        ax.set_title('各IP流量消耗', fontsize=14, fontweight='bold')
    
    # 5. 响应码与流量关系散点图
    ax = axes[4]
    scatter = ax.scatter(df['response_code'], df['bytes_sent'], 
                         c=df['response_code'], cmap='coolwarm', 
                         s=50, alpha=0.7, edgecolors='black')
    ax.set_title('Response Code vs Traffic', fontsize=14, fontweight='bold')
    ax.set_xlabel('Response Code')
    ax.set_ylabel('Traffic (bytes)')
    plt.colorbar(scatter, ax=ax)
    
    # 6. 请求大小分布直方图
    ax = axes[5]
    ax.hist(df['bytes_sent'], bins=10, color='green', edgecolor='black', alpha=0.7)
    ax.set_title('Request Size Distribution', fontsize=14, fontweight='bold')
    ax.set_xlabel('Traffic Size (bytes)')
    ax.set_ylabel('Frequency')
    
    # 设置整体标题
    plt.suptitle('Network Log Analysis Report', fontsize=18, fontweight='bold', y=0.98)
    
    # 调整布局
    plt.tight_layout()
    
    # 保存图表
    output_file = "network_logs_analysis.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✅ 图表已保存: {output_file}")
    
    # 显示图表
    plt.show()
    
    return output_file

def create_simple_charts(df):
    """创建简单的单独图表"""
    print("\n📊 创建单独图表文件...")
    
    # 1. IP访问频率图表
    plt.figure(figsize=(10, 6))
    ip_counts = df['ip_address'].value_counts()
    plt.bar(ip_counts.index, ip_counts.values, color='skyblue', edgecolor='black')
    plt.title('IP Address Access Frequency')
    plt.xlabel('IP Address')
    plt.ylabel('Access Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('ip_access_frequency.png', dpi=120)
    print("✅ ip_access_frequency.png 已保存")
    
    # 2. 响应码饼图
    plt.figure(figsize=(8, 8))
    response_counts = df['response_code'].value_counts()
    plt.pie(response_counts.values, labels=response_counts.index, autopct='%1.1f%%')
    plt.title('HTTP Response Code Distribution')
    plt.savefig('response_code_distribution.png', dpi=120)
    print("✅ response_code_distribution.png 已保存")
    
    plt.close('all')

def main():
    """主函数"""
    print("=" * 60)
    print("网络日志分析可视化工具")
    print("=" * 60)
    
    try:
        # 加载数据
        df = pd.read_csv('network_logs.csv')
        print(f"📈 加载了 {len(df)} 行数据")
        
        # 创建可视化
        chart_file = create_visualizations(df)
        
        # 创建简单图表
        create_simple_charts(df)
        
        print(f"\n🎯 可视化完成！")
        print(f"📁 生成文件:")
        print(f"   - {chart_file}")
        print(f"   - ip_access_frequency.png")
        print(f"   - response_code_distribution.png")
        
    except FileNotFoundError:
        print("❌ 错误：找不到 network_logs.csv 文件")
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    main()