#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs
from xml.dom.minidom import Document

#1 解决读取中问题
strf = ''
f = codecs.open('student.txt','r','utf-8')
s = f.readlines()
f.close()
for line in s:
    strf = strf + line
print(strf)

#2 写入xml中
doc = Document()
people = doc.createElement("root")
doc.appendChild(people)
aperson = doc.createElement("students")
people.appendChild(aperson)
name = doc.createElement("name")
aperson.appendChild(name)
personname = doc.createTextNode("\n"+strf+"\n")
name.appendChild(personname)
filename = "student.xml"
f = codecs.open(filename,'w','utf-8')
f.write(doc.toprettyxml(indent="  "))
f.close()