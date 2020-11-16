import codecs
import os
import os.path
import re

# 用于遍历.py文件内容,并确定关键字所在文件名
def findvcvarsall(path, keyword):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            findvcvarsall(os.path.join(path, file))
        elif os.path.splitext(file)[1] == '.py':  #将.py -> .txt就可以正常读取了.
            os.rename(os.path.join(path, file), os.path.join(path, file[0:len(file)-3]+'.txt'))
            with codecs.open(os.path.join(path, file[0:len(file)-3]+'.txt'), 'r', 'utf-8') as content:
                if re.search(keyword, content.read()):
                    print(os.path.join(path, file))
                content.close()


if __name__ == '__main__':
    findvcvarsall(r'C:\Users\seven\Desktop\distutils', 'Unable to find vcvarsall.bat')