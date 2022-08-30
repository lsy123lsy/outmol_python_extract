import os
import shutil
f2='D:\\MS'#存储文件夹
def CrossOver(dir,fl):
    for i in os.listdir(dir):  #遍历整个文件夹
        path = os.path.join(dir, i)
        if os.path.isfile(path):#判断是否为一个文件，排除文件夹
            if os.path.splitext(path)[1] == ".outmol":  # 判断文件扩展名是否为“.outmol”
                fl.append(i)
                shutil.move(os.path.abspath(path),f2)
        elif os.path.isdir(path):
            newdir=path
            CrossOver(newdir,fl)
    return fl
directory="D:\\1"  #原始文件夹名称
filelist=[]
output=CrossOver(directory,filelist)
for i in output:
    print(i)


