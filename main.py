"""
程序入口
演示三种导入方式
"""
import os

# ---- 导入方式1：从包直接导入类（推荐，最简洁）----
from file_tools import FileBackup

# ---- 导入方式2：从模块导入类 ----
# from file_tools.backup import FileBackup

# ---- 导入方式3：导入整个模块 ----
# from file_tools import backup
# backup.FileBackup(...)


if __name__ == "__main__":
    # 创建一个测试文件
    test_file = "example.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("这是一段测试内容")

    # 使用 FileBackup 类
    my_backup = FileBackup(test_file)

    # 备份到同目录
    my_backup.backup()

    # 备份到指定目录
    my_backup.backup(dest_dir="backups")
