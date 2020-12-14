from ftplib import FTP

#domain name or server ip:
ftp = FTP('192.168.1.10')
ftp.login(user='ftp', passwd = 'ftp')

dirname = input ("Delete folder: ")
try:
    ftp.cwd(dirname)                                            #check if file exists
except:
    print ("Directory does not exist on the server.")
else:
    delConfirm = input ("Are you sure [Y/N]: ")                 #asking confirmation
    if delConfirm == 'Y' or delConfirm == 'y':
        try:
            ftp.cwd('../') 
            ftp.rmd(dirname)
            print (dirname + " is deleted successfully.")
        except:
            print("Directory is not empty.")
    else:
        print (dirname + " is not deleted.")


ftp.quit()
