# coding=utf-8
'''
Created on 2020-7-1
只需第一次使用前运行一次
@author: 张印
'''
import io,os
from settings import GlobalConfig
def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with io.open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with io.open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

if __name__ == '__main__':
    root_dir = os.path.abspath(r".")
    print(root_dir)
    alter("settings.py","ROOTDIR=None",'ROOTDIR=r"%s"' % root_dir)