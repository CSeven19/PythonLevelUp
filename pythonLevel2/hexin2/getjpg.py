#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib.request
import os


# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html

def getImg(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    reg = r'img.*.src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

def cbk(a, b, c):
    '''''回调函数 
    @a:已经下载的数据块 
    @b:数据块的大小 
    @c:远程文件的大小 
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print
    '%.2f%%' % per

def saveImg(imglist):
    x = "a"
    for imgurl in imglist:
        dir = os.path.abspath('.')
        work_path = os.path.join(dir, x+'233441eew.jpg')
        urllib.request.urlretrieve(imgurl, work_path, cbk)
        x+="1"

if __name__ == "__main__":
    url = "https://tieba.baidu.com/p/5129822308"
    print(getImg(url))
    saveImg(getImg(url))