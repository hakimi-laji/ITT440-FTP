from ftplib import FTP

#domain name or server ip:
ftp = FTP('192.168.1.10')
ftp.login(user='ftp', passwd = 'ftp')

dirname = input ("New folder: ")
ftp.mkd(dirname)

ftp.quit()
