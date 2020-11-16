#-*- coding: utf-8 -*-
import base64, requests
# import codecs

# #1：查找文件时：
# fname = 'bingyu.pcm'
# with open(fname, 'rb') as f:
#     if b'some-pattern' in tmp: continue
#
# #2：使用socketl连接时：
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send(**b ** 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data);
#
# mysock.close()
#
# #3：提前进行编码：
# with open(fname, 'rb') as f:
#     lines = [x.decode('utf8').strip() for x in f.readlines()]

d = open('bingyu.pcm', 'rb').read()
data = {
    "format": "pcm",
    # "format": "wav",
    "rate": 16000,
    "channel": 1,
    "token": "your token",
    "cuid": "your mac",
    "len": len(d),
    "speech": base64.b64encode(d).replace('\n', '')
}
result = requests.post('http://vop.baidu.com/server_api', json=data, headers={'Content-Type': 'application/json'})
data_result = result.json()
print(data_result['err_msg'])
if data_result['err_msg']=='success.':
    print("语音结果：" + data_result['result'][0].encode('utf-8'))
else:
    print(data_result)