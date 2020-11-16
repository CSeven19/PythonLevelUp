#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import re
import sqlite3

#1 re.match(pattern, string, flags=0) e.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# import re
#
# line = "总计：63.30元"
# matchObj = re.match(r'(.*)总计：(.*?)元', line, re.M|re.I)
#
# #  matchObj.group(1)代表第一个(.*)内容
# #  matchObj.group(2)代表第二个(.*?)内容
# if matchObj:
#    print("matchObj.group() : ", matchObj.group())
#    print("matchObj.group(1) : ", matchObj.group(1))
#    print("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print("No match!!")

def read_xlsx(filename,sheetname):
    workbook = xlrd.open_workbook(filename)
    booksheet = workbook.sheet_by_name(sheetname)
    cost = 0.0
    p = list()
    for row in range(booksheet.nrows):
        row_data = []
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            try:
                val = cel.value
                val = re.sub(r'\s+', '', val)
                # print(val)
                matchObj = re.match(r'(.*)总计：(.*?)元', val, re.M | re.I)
                if matchObj:
                    # print(matchObj.group(2))
                    # print(type(matchObj.group(2)))
                    # print(float(matchObj.group(2)))
                    cost = float(matchObj.group(2))
            except:
                pass

            if type(val) == float:
                val = int(val)
            else:
                val = str(val)
            row_data.append(val)
        p.append(row_data)

    # print(p)
    print(cost)
    return p


def operat_sqlite(*data):
    # print(type(data))
    # print(data)
    print(data[0])
    try:
        conn = sqlite3.connect('E:\list.db')
    except:
        print('open sqlite3 failed.')
        return
    else:  # 操作数据库
        c = conn.cursor()
        for item in data:
            for i in range(len(item)):
                DLDMv = item[i][1]
                LDDMv = item[i][3]
                LDMCv = item[i][2]
                FHSSLXv = item[i][5]
                XZQHv = item[i][6]
                try:
                    # creat sql
                    c.execute("insert into roadkey (DLDM, LDDM, LDMC, FHSSLX, XZQH) values (?, ?, ?, ?, ?)",
                              (DLDMv, LDDMv, LDMCv, FHSSLXv, XZQHv))
                    conn.commit()
                except:
                    print('insert roadky failed ')
                    pass
                print(i)
                print(item[i])
        conn.close()

    return


if __name__ == '__main__':
    data_list = list()
    data_list = read_xlsx('个人账单.xls','手机账单')
    # operat_sqlite(data_list)