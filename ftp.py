from ftplib import FTP
import os

#get domain name or server ip:
ftpdomain = input ("FTP domain (default: 192.168.1.10)\n>>> ")
ftp = FTP(ftpdomain)

#authenticate user
authUser = input ("Username: ")
authPass = input ("Password: ")
ftp.login(user = authUser, passwd = authPass)

os.chdir("/home/nox/ftp") #make sure to change this client directory a.k.a. this machine's

#GET command
def ftpGet():
    filename = input ("\nFile to retrieve: ")
    localfile = open(filename, 'wb')                            #file to retrieve
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)   #retrieve the file
    localfile.close()
    
#PUT command
def ftpPut():
    filename = input ("\nFile to send: ")
    localfile = open(filename2, 'rb')                  # file to send
    ftp.storbinary('STOR ' + filename, localfile)     # send the file
    localfile.close()

#LIST command
def ftpList():
    print ('\nFiles in the directory:\n------------------------------------------------------------')
    print ('Permission                            Size Date   Time  Name')
    files = ftp.dir()

menu = ''
ftpList()
while menu != 'X' or menu != 'x':
    menu = input ("\nWELCOME, " + authUser +" \n [G]et a file from server \n [P]ut a file into server \n [L]ist all files in server \n\t\t\t\tE[X]IT \n\n>>>")
    if menu == 'G' or menu == 'g':
        ftpGet()
    elif menu == 'P' or menu == 'p':
        ftpPut()
    elif menu == 'L' or menu == 'l':
        ftpList()
    elif menu == 'X' or menu == 'x':
        print ("Goodbye!")
        break
    else:
        print ("***PLEASE INPUT A KEY***")
    
ftp.quit()

