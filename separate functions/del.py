from ftplib import FTP

#domain name or server ip:
ftp = FTP('192.168.1.10')
ftp.login(user='ftp', passwd = 'ftp')

filename = input ("File to delete: ")
ftp.delete(filename)

ftp.quit()


