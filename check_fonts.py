# check_fonts.py
import os

# 常见中文字体文件
common_fonts = [
    "C:/Windows/Fonts/simhei.ttf",   # 黑体
    "C:/Windows/Fonts/msyh.ttc",     # 微软雅黑
    "C:/Windows/Fonts/msyhbd.ttc",   # 微软雅黑粗体
    "C:/Windows/Fonts/simsun.ttc",   # 宋体
    "C:/Windows/Fonts/simkai.ttf",   # 楷体
    "C:/Windows/Fonts/simfang.ttf",  # 仿宋
    "C:/Windows/Fonts/simli.ttf",    # 隶书
]

print("检查系统中常见中文字体：")
print("=" * 60)

found_fonts = []
for font in common_fonts:
    if os.path.exists(font):
        print(f"✅ 找到: {font}")
        found_fonts.append(font)
    else:
        print(f"❌ 没有: {font}")

print("\n" + "=" * 60)
print(f"总共找到 {len(found_fonts)} 种中文字体")

if found_fonts:
    print("\n建议使用：")
    for font in found_fonts[:3]:  # 显示前3个
        print(f"  {font}")
else:
    print("\n⚠️  未找到任何常见中文字体，可能需要使用英文字体")