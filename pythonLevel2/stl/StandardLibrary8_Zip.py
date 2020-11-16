# # zip
# #
# # 8.1 zipfile
# #!/usr/bin/env python3
# import os,zipfile
# def Zip(target_dir):
#     target_file=os.path.basename(os.getcwd())+'.zip'
#     zip_opt=input("Will you zip all the files in this dir?(Choose 'n' you should add files by hand)y/n: ")
#     while True:
#         if zip_opt=='y':       #compress all the files in this dir
#             filenames=os.listdir(os.getcwd())    #get the file-list of this dir  #1设置from/to参数。
#             zipfiles=zipfile.ZipFile(os.path.join(target_dir,target_file),'w',compression=zipfile.ZIP_DEFLATED)  #2获取zipfile对象
#             for files in filenames:
#                 zipfiles.write(files)  #3压缩
#             zipfiles.close()
#             print("Zip finished!")
#             break
#         elif zip_opt=='n':     #compress part of files of this dir
#             filenames=list(input("Please input the files' name you wanna zip:"))
#             zipfiles=zipfile.ZipFile(os.path.join(target_dir,target_file),'w',compression=zipfile.ZIP_DEFLATED)
#             for files in filenames:
#                 zipfiles.write(files)
#             zipfiles.close()
#             print("Zip finished!")
#             break
#         else:
#             print("Please in put the character 'y' or 'n'")
#             zip_opt=input("Will you zip all the files in this dir?(Choose 'n' you should add files by hand)y/n: ")
# def Unzip(target_dir):
#     target_name=input("Please input the file you wanna unzip:")
#     zipfiles=zipfile.ZipFile(target_name,'r')
#     zipfiles.extractall(os.path.join(target_dir,os.path.splitext(target_name)[0]))
#     zipfiles.close()
#     print("Unzip finished!")
# def main():
#     opt=input("What are you gonna do?Zip choose 'y',unzip choose 'n'.y/n: ")
#     while True:
#         if opt=='y':  #compress files
#             zip_dir=input("Please input the absdir you wanna put the zip file in:")
#             Zip(zip_dir)
#             break
#         elif opt=='n':  #unzip files
#             unzip_dir=input("Please input the absdir you wanna put the zip file in(Nothing should be done if you wann unzip files in the current dir):")
#             if unzip_dir=='':
#                 Unzip(os.getcwd())
#             else:
#                 Unzip(unzip_dir)
#             break
#         else:
#             print("Please input the character 'y' or 'n'")
#             opt=input("What are you gonna do?Zip choose 'y',unzip choose 'n'.y/n: ")
# if __name__=='__main__':
#     main()

# # 8.2 zipimport 载入zip包中的模板
# import sys
# import zipfile
# if __name__ == '__main__':
#     zf = zipfile.PyZipFile('zipimport_example.zip', mode='w')
# try:
#     zf.writepy('.')  #将当前目录下所有文件生成pyc文件写入zip包中.
#     zf.write('StandardLibrary1_String.py')  #将'StandardLibrary1_String.py'写入zip中
#     zf.write('example/two.txt')
# finally:
#     zf.close()
# for name in zf.namelist():
#     print(name)
# import zipimport
# importer = zipimport.zipimporter('zipimport_example.zip')
# for module_name in ['hexin2chapter17_Web', 'not_there']:
#     print(module_name, ':', importer.find_module(module_name))
#     code = importer.get_code(module_name)
#     print(code)
#     source = importer.get_source(module_name)
#     print(source)
#     print(module_name, importer.is_package(module_name))
#     importer.load_module(module_name)
