from ftplib import FTP

#domain name or server ip:
ftp = FTP('192.168.1.10')
ftp.login(user='ftp', passwd = 'ftp')

pathname = 'none'
ftp.dir()

# type folder name to move
# type / to move to home
# type ../ to move one directory up

while pathname != '':
    if pathname != '':
        pathname = input ("Go where: ")
        ftp.cwd(pathname)
        ftp.dir()
        print (ftp.pwd())
    else:
        ftp.quit()