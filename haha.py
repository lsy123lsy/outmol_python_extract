import os
import re

""" name = os.path.splitext():分离文件名(name[0])和后缀name[1]
    os.rename(new_filename, old_filename):修改文件名，若不在最初工作地址则需更改
    os.listdir(文件地址)：得到当前目录的所有文件以及文件夹（file）
    os.path.join(根文件地址, file)：得到file的绝对地址
    os.path.isdir(file的绝对地址)：判断是否为文件夹（isfile判断是否为文件）
    os.chdir(根文件地址)：修改根文件地址
    os.getcwd()：得到当前工作地址
"""
import os


def renaming(file):
    """修改后缀"""
    ext = os.path.splitext(file)  # 将文件名路径与后缀名分开

    if ext[1] == '.outmol':  # 文件名：ext[0]
        new_name = ext[0] + '.txt'  # 文件后缀：ext[1]
        os.rename(file, new_name)  # tree()已切换工作地址，直接替换后缀
    elif ext[1] == '.txt':
        new_name = ext[0] + '.txt'
        os.rename(file, new_name)


def tree(path):
    """递归函数"""
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    for file in files:
        file_path = os.path.join(path, file)  # 获取该文件的绝对路径
        if os.path.isdir(file_path):  # 判断是否为文件夹
            tree(file_path)  # 开始递归
        else:
            os.chdir(path)  # 修改工作地址（相当于文件指针到指定文件目录地址）
            renaming(file)  # 修改后缀


path = "D:\\MS\\"  # 找到txt所在位置
tree(path)
files = os.listdir(path)  # 得到文件夹下所有txt
i = 0  # 定义变量
for file in files:  # 让txt循环起来
    i += 1  # 用于后续查看完成进度
    position = path + '\\' + file  # 构造绝对路径
    # print(position)
    f1 = open(position, "r", encoding='utf-8')  # 打开并读取文件信息
    data = f1.read()  # 读取信息
    #print(data)
    parrern = r"Fermi Energy\:\s*[-]?\d+\.\d+ Ha\s*[-]?\d+\.\d+ eV\s*\-kTS\_e\=\s*[-]?\d+\.\d+Ha\nDFT energy gap\:\s*[-]?\d+\.\d+ Ha\s*[-]?\d+\.\d+ eV\nvalence band edge\:\s*[-]?\d+\.\d+ Ha\s*[-]?\d+\.\d+ eV\nconduction band edge\:\s*[-]?\d+\.\d+ Ha\s*[-]?\d+\.\d+ eV\n"  # 用正则匹配feimiEnergy

    str2 = re.findall(parrern, data)  # 查找所有符合条件的信息
    print(str2[-1])
    f2 = open("提取的信息.txt", "a+", encoding="utf-8")  # 打开并写入信息
    # print(";".join(str2).replace(";", "\n"))
    ext = os.path.splitext(file)
    f2.write(ext[0]+"\n")
    #f2.write(";".join(str2).replace(";", "\n") + "\n")  # 先转为非数组类型，再用分行输出
    f2.write(str2[-1])#输出最后一个
    print("完成" + str(i))
    f2.close()  # 有开就有关
    f1.close()  # 有开就有关
