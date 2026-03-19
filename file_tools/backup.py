"""
文件备份模块
只负责备份逻辑，不包含任何运行入口
"""
import os
import shutil
from datetime import datetime


class FileBackup:
    """
    文件备份类
    作用：把指定文件复制一份，当作备份
    """

    def __init__(self, source_path):
        """
        创建备份器时，告诉它要备份哪个文件
        例如：backup = FileBackup("我的文档.txt")
        """
        self.source_path = source_path

    def backup(self, dest_dir=None):
        """
        执行备份
        如果不写 dest_dir，就备份到原文件所在的文件夹
        """
        # 第1步：检查源文件是否存在
        if not os.path.exists(self.source_path):
            print("错误：找不到这个文件！")
            return None

        # 第2步：决定备份文件叫什么名字
        filename = os.path.basename(self.source_path)
        name_part = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = name_part + "_backup_" + timestamp + ext

        # 第3步：决定备份文件放在哪里
        if dest_dir is None:
            dest_dir = os.path.dirname(self.source_path)
            if dest_dir == "":
                dest_dir = "."
        backup_path = os.path.join(dest_dir, backup_filename)

        # 第4步：确保目标文件夹存在
        os.makedirs(dest_dir, exist_ok=True)

        # 第5步：复制文件
        shutil.copy2(self.source_path, backup_path)
        print("备份完成！新文件在：", backup_path)
        return backup_path
