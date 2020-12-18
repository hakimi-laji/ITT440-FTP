# ITT440-FTP
Individual project - Basic FTP in Python
by MUHAMMAD HAKIMI BIN MOHD LAJI (2019290708)

WHY?
1. I need to pass this subject.
2. FTP on Linux is great but can be difficult to use sometimes. My code aimed to simplify everything.

WATCH HOW IT WORKS:
https://youtu.be/9prZGHpJuCc


For this to work, you will need an FTP domain. You can use a Linux machine as a server by following the guide below

https://www.techrepublic.com/article/how-to-quickly-setup-an-ftp-server-on-ubuntu-18-04/

(All credits belong to the writer/website)


HOW?
1. Get the server up and running
2. Run the code on client with python3

TROUBLESHOOT
1. Make sure the firewall on both server and client allowed the FTP connection
2. Log into a valid user account on the server side

For now, the functions are severely lacking. What works are:
- retrieve single file
- send single file   
- list files
- move between directory
- rename file 
- create/remove directory
- error handling
- hide password inputs

What I want to add:
- retrieve multiple files
- send multiple files
- force delete non-empty directory
- security stuffs (like traffic encryption)
- etc...
