from ftplib import FTP
import os
import getpass

#get domain name or server ip:
ftp = FTP(ftpdomain)

#authenticate user
authUser = input ("Username: ")
password = getpass.getpass()
authPass = password
ftp.login(user = authUser, passwd = authPass)

#save location - this is where the files downloaded will be saved
#savePath = '/home/nox/ftp'
#os.chdir(savePath)

#save location is set to current working directory - the same directory where this .py is located
os.getcwd()

#GET command
def ftpGet():
    filename = input ("File to retrieve: ")
    try:
        localfile = open(filename, 'wb')                            #file to retrieve
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)   #retrieve the file
        print (filename + " is retrieved successfully.")
        localfile.close()
    except:
        print ("File does not exist on the server. Retrieval unsuccessful.")
        os.remove(filename)
    
#PUT command
def ftpPut():
    filename = input ("File to send: ")
    try:
        localfile = open(filename, 'rb')                            # file to send
        ftp.storbinary('STOR ' + filename, localfile)               # send the file
        print (filename + " is uploaded successfully.")
        localfile.close()
    except:
        print ("File does not exist on the current directory. Upload unsuccessful.")
    
#DEL command
def ftpDel():
    filename = input ("File to delete: ")                           #select file to delete
    try:
        ftp.size(filename)                                          #check if file exists
    except:
        print ("File does not exist on the server.")
    else:
        delConfirm = input ("Are you sure [Y/N]: ")                 #asking confirmation
        if delConfirm == 'Y' or delConfirm == 'y':
            ftp.delete(filename)
            print (filename + " is deleted successfully.")
        else:
            print (filename + " is not deleted.")
        
#RENAME command
def ftpRename():
    filename = input ("File to rename: ")                           #file to rename
    try:
        ftp.size(filename)                                          #check if file exists
    except:
        print ("File does not exist on the server")
    else:
        newname = input ("New name: ")                              #new name file
        ftp.rename(filename, newname)
        print (filename + " is renamed to " + newname)

#LIST command
def ftpList():
    print ("\nDIRECTORY: home/" + authUser + ftp.pwd() + "\n------------------------------------------------------------")
    print ('Permission                            Size Date   Time  Name')
    ftp.dir()

#MOVE between directories command
def ftpDirMove():
    pathname = input ("Move to directory: ")                        #folder to enter
    try:
        ftp.cwd(pathname)                                           #check if folder exists
    except:
        print ("Directory does not exist.")
    else:
        ftpList()

#RETURN to previous directoy command
def ftpDirReturn():
    ftp.cwd("../")                                                  #return to previous directory
    ftpList()
    
#RETURN to home command
def ftpDirHome():
    ftp.cwd("/")                                                    #return to home directory
    ftpList()
    
#CREATE new directory command
def ftpDirNew():
    dirname = input ("Create new folder: ")                         #folder name to create
    ftp.mkd(dirname)

#DELETE a directory
def ftpDirDel():
    dirname = input ("Delete a folder: ")
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

# ^^^ FUNCTIONS ABOVE ^^^           vvv INTERFACE BELOW vvv #

#Main menu user interface
print ("\nWELCOME, " + authUser)                                    #greetings message
ftpList()                                                           #display files on server on initial login

menu = ''
while menu != 'X' or menu != 'x':
    print ("""
  / FTP MENU \-------------------------------------< E[X]IT >
 [1] List all files        [Q] Move to a different directory
 [2] Get a file            [W] Return to previous directory
 [3] Put a file            [E] Return to home directory
 [4] Delete a file         [A] Create a new folder
 [5] Rename a file         [S] Delete a folder
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
    elif menu == 'A' or menu == 'a':
        ftpDirNew()
    elif menu == 'S' or menu == 's':
        ftpDirDel()
    elif menu == 'X' or menu == 'x':
        print ("Goodbye!\n")
        break
    else:
        print ("***PLEASE INPUT A VALID KEY***")
    
ftp.quit()

