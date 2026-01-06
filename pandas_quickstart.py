import pandas as pd
# 读取csv文件
df = pd.read_csv('network_logs.csv')
print("1.数据加载完成")
print(f"    数据形状：{df.shape} 行 x {df.shape[1]} 列")
print()
# 查看数据
print("2.数据预览：")
print(df.head(3))
print()
# 查看列信息
print("3.列信息:")
print(f"    列名：{list(df.columns)}")
print()
# 基本统计
print("4. 数值列统计:")
print(df.describe())
print()
# 选择列的不同方式
print("5. 选择列的三种方式:")
print("   A. df['ip_address'] - 返回Series")
print("   B. df[['ip_address', 'response_code']] - 返回DataFrame")
print("   C. df.ip_address - 属性方式（不推荐，有局限性）")
# 过滤数据
print("\n6. 过滤示例：只显示响应码为200的行")
print(df[df['response_code'] == 200].head(3))
