from ftplib import FTP
import os

#get domain name or server ip:
ftpdomain = input ("FTP domain (default: 192.168.1.10)\n>>> ")
ftp = FTP(ftpdomain)

#authenticate user
authUser = input ("Username: ")
authPass = input ("Password: ")
ftp.login(user = authUser, passwd = authPass)

#save location - this is where the files downloaded will be saved
savePath = '/home/nox/ftp'
os.chdir(savePath)

#GET command
def ftpGet():
    filename = input ("\nFile to retrieve: ")
    localfile = open(filename, 'wb')                            #file to retrieve
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)   #retrieve the file
    print (filename + " is retrieved successfully")
    localfile.close()
    
#PUT command
def ftpPut():
    filename = input ("\nFile to send: ")
    localfile = open(filename, 'rb')                  # file to send
    ftp.storbinary('STOR ' + filename, localfile)     # send the file
    print (filename + " is uploaded successfully")
    localfile.close()
    
#DEL command
def ftpDel():
    filename = input ("File to delete: ")           #file to delete
    delConfirm = input ("Are you sure [y/n]: ")     #asking confirmation
    if delConfirm == 'Y' or delConfirm == 'y':
        ftp.delete(filename)
        print (filename + " is deleted successfully")
    else:
        print (filename + " is not deleted")
        
#RENAME command
def ftpRename():
    filename = input ("File to rename: ")           #file to rename
    newname = input ("New name: ")                  #new name file
    ftp.rename(filename, newname)
    print (filename + " is renamed to " + newname)

#LIST command
def ftpList():
    print ("\nDIRECTORY: home/" + authUser + ftp.pwd() + "\n------------------------------------------------------------")
    print ('Permission                            Size Date   Time  Name')
    ftp.dir()

#MOVE between directories command
def ftpDirMove():
    pathname = input ("Move to directory: ")
    ftp.cwd(pathname)
    ftpList()

#RETURN to previous directoy command
def ftpDirReturn():
    ftp.cwd("../")
    ftpList()
    
#RETURN to home command
def ftpDirHome():
    ftp.cwd("/")
    ftpList()
    

#Main menu user interface
print ("\nWELCOME, " + authUser)    #greetings message
ftpList()                           #display files on server
menu = ''
while menu != 'X' or menu != 'x':
    print ("""
  / FTP MENU \--------------------------------------------------< E[X]IT
 [1] List all files on the server    | [Q] Move to a different directory
 [2] Get a file from server          | [W] Return to previous directory
 [3] Put a file into server          | [E] Return to home directory
 [4] Delete a file                   | [A] Create a new folder
 [5] Rename a file                   | [S] Delete a folder
    """)
    menu = input ("-> ")
    if menu == '1':
        ftpList()
    elif menu == '2':
        ftpGet()
    elif menu == '3':
        ftpPut()
    elif menu == '4':
        ftpDel()
    elif menu == '5':
        ftpRename()
    elif menu == 'Q' or menu == 'q':
        ftpDirMove()
    elif menu == 'W' or menu == 'w':
        ftpDirReturn()
    elif menu == 'E' or menu == 'e':
        ftpDirHome()
    elif menu == 'X' or menu == 'x':
        print ("Goodbye!\n")
        break
    else:
        print ("***PLEASE INPUT A KEY***")
    
ftp.quit()

