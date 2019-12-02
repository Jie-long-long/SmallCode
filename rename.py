# —*— coding:utf-8 _*_

import os
path = input('请输入文件路径(结尾加上/)：')
prefix = input('请输入新文件名前缀：')

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0
for i in f:
  oldname = path + f[n]  # 设置旧文件名(路径+文件名)
  newname = path + prefix + '-' + str(n+1) + '.txt'  # 设置新文件名
  os.rename(oldname,newname)  # 用os模块中的rename方法对文件改名
  print(oldname,'=====>',newname)
  n+=1
