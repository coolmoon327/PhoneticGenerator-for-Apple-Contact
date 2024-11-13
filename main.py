import argparse
import os
from PhoneticGenerator import PhoneticGenerator

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description='处理 iPhone 联系人 VCF 文件，提取姓和名的拼音并添加到 X-PHONETIC 字段'
    )
    parser.add_argument('vcf_file', metavar='VCF_FILE', type=str, help='VCF 文件路径')

    # 解析命令行参数
    args = parser.parse_args()

    # 检查文件是否存在
    if not os.path.isfile(args.vcf_file):
        print(f"错误：指定的文件 '{args.vcf_file}' 不存在或不是一个有效的文件。")
        return

    try:
        # 创建 PhoneticGenerator 对象并转换 VCF 文件
        generator = PhoneticGenerator(args.vcf_file)
        generator.convert()
        print(f"VCF 文件已成功处理并保存到: {args.vcf_file}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == '__main__':
    main()
