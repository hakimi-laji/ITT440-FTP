from ftplib import FTP

#domain name or server ip:
ftp = FTP('192.168.1.10')
ftp.login(user='ftp', passwd = 'ftp')

filename = input ("File to send: ")
localfile = open(filename, 'rb')                  # file to send
ftp.storbinary('STOR ' + filename, localfile)     # send the file
localfile.close()

ftp.quit()