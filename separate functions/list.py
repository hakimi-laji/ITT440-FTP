from ftplib import FTP
import os # allows me to use os.chdir

port=21
ip="192.168.1.10"
password='ftp'

os.chdir("/home/nox") #changes the active dir - this is where downloaded files will be saved to
ftp = FTP("192.168.1.10")
ftp.login('ftp',password)

print ('Files in the directory:\n------------------------------------------------------------')
print ('Permission    File No.                Size Date   Time  Name')

ftp.dir()

