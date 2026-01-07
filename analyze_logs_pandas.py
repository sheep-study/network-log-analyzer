import pandas as pd
def analyze_with_pandas(log_file):
    """
        使用Pandas进行日志分析
        参数:log_file - 日志文件路径
        返回:包含所有统计结果的字典
    """
# 1. 加载数据
    df = pd.read_csv(log_file)
    print(f"📊 加载了 {len(df)} 行数据")
    results = {}

# 2. IP统计
    ip_counts = df['ip_address'].value_counts()
    results['ip_stats'] = {
        'total_requests': len(df),
        'unique_ips': ip_counts.shape[0],
        'most_common_ip': ip_counts.index[0],
        'most_common_count': ip_counts.iloc[0],
        'ip_counts': ip_counts
    }
# 3. 响应码统计
    response_counts = df['response_code'].value_counts()
    results['response_stats'] = {
        'response_counts': response_counts
    }
# 4. 流量统计
    total_bytes = df['bytes_sent'].sum()
    results['traffic_stats'] = {
        'total_bytes': total_bytes,
        'avg_bytes_per_request': total_bytes / len(df)
    }
# 5. 按IP分组统计
    ip_traffic = df.groupby('ip_address')['bytes_sent'].sum().sort_values(ascending=False)
    results['ip_traffic'] = ip_traffic
 # 6. 时间分析
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    hourly_counts = df.groupby('hour').size()
    results['hourly_stats'] = hourly_counts
    return results,df

def print_pandas_results(results):
    """打印分析结果"""
    print("\n📈 分析结果汇总")
    print("=" * 60)
    
# IP统计
    print("\n1. IP地址统计:")
    print("-" * 40)
    ip_stats = results['ip_stats']
    print(f"总请求数: {ip_stats['total_requests']}")
    print(f"唯一IP数: {ip_stats['unique_ips']}")
    print(f"最活跃IP: {ip_stats['most_common_ip']} (访问{ip_stats['most_common_count']}次)")
    print("\nIP访问频率TOP 5:")
    for ip, count in results['ip_stats']['ip_counts'].head().items():
        print(f"  {ip:<15} : {count}次")
# 响应码统计
    print("\n2.HTTP响应码统计:")
    print("-" * 40)
    for code,count in results['response_stats']['response_counts'].items():
        percentage = (count / ip_stats['total_requests']) * 100
        print(f"  响应码 {code}: {count:3d}次 ({percentage:5.1f}%)")
# 流量统计
    print("\n3. 流量统计:")
    print("-" * 40)
    traffic = results['traffic_stats']
    print(f"总流量: {traffic['total_bytes']:,} bytes")
    print(f"平均每请求: {traffic['avg_bytes_per_request']:.1f} bytes")
# IP流量排名
    print("\n4. IP流量消耗TOP 3:")
    print("-" * 40)
    for ip, traffic in results['ip_traffic'].head(3).items():
        print(f"  {ip:<15} : {traffic:,} bytes")
# 小时统计
    print("\n5. 按小时访问量:")
    print("-" * 40)
    for hour, count in results['hourly_stats'].items():
        print(f"  小时 {hour:02d}:00 - {count:2d}次请求")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # 运行分析
    results, df = analyze_with_pandas('network_logs.csv')
    
    # 打印结果
    print_pandas_results(results)
    
    # 额外：显示原始DataFrame的更多信息
    print("\n🔍 原始数据信息:")
    print(f"数据形状: {df.shape}")
    print(f"列数据类型:\n{df.dtypes}")
    
    # 保存统计结果到CSV
    print("\n💾 保存统计结果到文件...")
    results['ip_stats']['ip_counts'].to_csv('ip_statistics.csv')
    results['response_stats']['response_counts'].to_csv('response_statistics.csv')
    results['ip_traffic'].to_csv('ip_traffic.csv')
    
    print("✅ 分析完成！")
    print("📁 已保存文件: ip_statistics.csv, response_statistics.csv, ip_traffic.csv")