 #!/usr/bin/env python

# #1 ftp 客户程序
# import ftplib
# import os
# import socket
#
# HOST = 'ftrans.chieru.co.jp'
# DIRN = 'CaLaboLanguage/v1.1/20170605'
# FILE = 'languagelib.zip'
#
# def main():
#     try:
#      f = ftplib.FTP(HOST)
#     except (socket.error, socket.gaierror) as e:
#         print('ERROR: cannot reach "%s"'% HOST)
#         return
#     print('*** Connected to host "%s"'% HOST)
#
#     try:
#         f.login('adtis_dev','gG5Wxfdc')
#     except ftplib.error_perm:
#         print('ERROR: cannot login anonymously')
#         f.quit()
#         return
#     print('*** Logged in as "anonymous"')
#
#     try:
#         f.cwd(DIRN)
#     except ftplib.error_perm:
#         print('ERROR: cannot CD to "%s"' % DIRN)
#         f.quit()
#         return
#     print('*** Changed to "%s" folder' % DIRN)
#
#     try:
#         f.retrbinary('RETR %s' % FILE,open(FILE, 'wb').write)
#     except ftplib.error_perm:
#         print('ERROR: cannot read file "%s"' % FILE)
#         os.unlink(FILE)
#     else:
#         print('*** Downloaded "%s" to CWD' % FILE)
#         f.quit()
#         return
#
# if __name__ == '__main__':
#     main()

# #2 NNTP
# import nntplib
# import socket
#
# HOST = 'your.nntp.server'
# GRNM = 'comp.lang.python'
# USER = 'wesley'
# PASS = 'youllNeverGuess'
#
# def main():
#
#     try:
#         n = nntplib.NNTP(HOST)
#         #, user=USER, password=PASS)
#     except socket.gaierror as e:
#         print('ERROR: cannot reach host "%s"' % HOST)
#         print(' ("%s")' % eval(str(e))[1])
#         return
#     except nntplib.NNTPPermanentError as e:
#         print('ERROR: access denied on "%s"' % HOST)
#         print(' ("%s")' % str(e))
#         return
#     print('*** Connected to host "%s"' % HOST)
#
#     try:
#         rsp, ct, fst, lst, grp = n.group(GRNM)
#     except nntplib.NNTPTemporaryError as e2:
#         print('ERROR: cannot load group "%s"' % GRNM)
#         print(' ("%s")' % str(e2))
#         print(' Server may require authentication')
#         print(' Uncomment/edit login line above')
#         n.quit()
#         return
#     except nntplib.NNTPTemporaryError as e3:
#         print('ERROR: group "%s" unavailable' % GRNM)
#         print(' ("%s")' % str(e3))
#         n.quit()
#         return
#     print('*** Found newsgroup "%s"' % GRNM)
#
#     rng = '%s-%s' % (lst, lst)
#     rsp, frm = n.xhdr('from', rng)
#     rsp, sub = n.xhdr('subject', rng)
#     rsp, dat = n.xhdr('date', rng)
#     print ('''*** Found last article (#%s):
#     From: %s
#     Subject: %s
#     Date: %s
# '''% (lst, frm[0][1], sub[0][1], dat[0][1]))
#
#     rsp, anum, mid, data = n.body(lst)
#     displayFirst20(data)
#     n.quit()
#
# def displayFirst20(data):
#     print('*** First (<= 20) meaningful lines:\n')
#     count = 0
#     lines = (line.rstrip() for line in data)
#     lastBlank = True
#     for line in lines:
#         if line:
#             lower = line.lower()
#             if (lower.startswith('>') and not \
#                 lower.startswith('>>>')) or \
#                 lower.startswith('|') or \
#                 lower.startswith('in article') or \
#                 lower.endswith('writes:') or \
#                 lower.endswith('wrote:'):
#                     continue
#             if not lastBlank or (lastBlank and line):
#                 print(' %s' % line)
#                 if line:
#                     count += 1
#                     lastBlank = False
#                 else:
#                     lastBlank = True
#             if count == 20:
#              break
#
# if __name__ == '__main__':
#     main()


# #3  SMTP POP3 EXAMPLE
#
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = '***'
# receiver = '***'
# subject = 'python email test'
# smtpserver = 'smtp.163.com'
# username = '***'
# password = '***'
#
# msg = MIMEText('你好', 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
# msg['Subject'] = Header(subject, 'utf-8')
#
# smtp = smtplib.SMTP()
# smtp.connect('smtp.163.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()

#4