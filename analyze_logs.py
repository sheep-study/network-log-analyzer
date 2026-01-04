import csv
from collections import defaultdict
print("===开始分析网络日志===")
print()

def count_ip_frequency(log_file):
    """
    统计每个IP地址出现的次数
    参数：
        log_file:日志文件路径
    返回：
        ip_counter:字典,键是IP地址,值是出现次数
    """
    # 统计IP频率的函数
    ip_counter = defaultdict(int)
    try:
        with open(log_file,'r',encoding='utf-8') as file:
            print("文件打开成功，开始读取...")
            reader = csv.DictReader(file)
            for row in reader:
                ip_address = row['ip_address']
                ip_counter[ip_address] += 1
            print(f"读取完成，共处理了{len(ip_counter)}个不同的IP地址。")
    except Exception as e:
        print(f"在读取文件时发生错误：{e}")
    return ip_counter
# 定义排序和显示结果的函数
def display_results1(ip_counter):
    """
    显示IP频率统计结果
    参数：
        ip_counter: 统计好的IP频率字典
    """
    print("IP地址访问频率统计:")
    print("-" * 40)
    # 按访问次数从高到低
    # sorted函数：对字典项进行排序
    # key=lambda x: x[1]：按每个元组的第二个元素（次数）排序
    # reverse=True：降序排列
    sorted_ips = sorted(ip_counter.items(),key=lambda x: x[1],reverse=True)
    for ip,count in sorted_ips:
        print(f"IP地址:{ip:<15}访问次数：{count}")
    print("-" * 40)
    
    total_requests = sum(ip_counter.values())
    unique_ips = len(ip_counter)
    print(f"总请求数: {total_requests}")
    print(f"唯一IP数: {unique_ips}")
    if sorted_ips:
        most_common_ip,most_common_count = sorted_ips[0]
        print(f"最活跃IP: {most_common_ip} (访问{most_common_count}次)")
    print()

# 统计HTTP响应码频率
def count_response_codes(log_file):
    response_counter = defaultdict(int)

    with open(log_file,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = row['response_code']
            response_counter[code] += 1
        return response_counter
def display_results2(response_counter):
    print("HTTP响应码频率统计:")
    print("-" * 40)
    sorted_responses = sorted(response_counter.items(),key=lambda x: x[1],reverse=True)
    for code,count in sorted_responses:
        print(f"HTTP响应码:{code:<15}访问次数：{count}")
    print("-" * 40)
    
    total_requests = sum(response_counter.values())
    unique_responses = len(response_counter)
    print(f"总请求数: {total_requests}")
    print(f"唯一HTTP数: {unique_responses}")
    if sorted_responses:
        most_common_response,most_common_count = sorted_responses[0]
        print(f"最活跃HTTP: {most_common_response} (访问{most_common_count}次)")
    print()

# 计算总流量
def calculate_total_traffic(log_file):
    total_bytes = 0
    with open(log_file,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                bytes_sent = int(row['bytes_sent'])
                total_bytes += bytes_sent
            except ValueError:
                continue
    return total_bytes
def display_results3(total_bytes):
    print("-" * 40)

    print(f"总流量：{total_bytes} bytes")

if __name__ == "__main__":
    """
    这是Python程序的主入口
    当直接运行这个文件时，下面的代码会被执行
    """

    # 指定日志文件路径
    log_file = "network_logs.csv"
    try:
        print("正在读取日志文件...")
        ip_counter = count_ip_frequency(log_file)
        response_counter = count_response_codes(log_file)
        total_bytes = calculate_total_traffic(log_file)
        
        display_results1(ip_counter)
        display_results2( response_counter)
        display_results3( total_bytes)


        print("=== 分析完成 ===")
    except FileNotFoundError:
        print(f"错误：找不到文件 '{log_file}'")
        print("请确保network_logs.csv文件在当前目录下")
    except Exception as e:
        print(f"发生错误: {e}")