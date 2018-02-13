#!/usr/bin/python
import subprocess as sp
import getpass
from pexpect import pxssh
try:
    array = []
    s = pxssh.pxssh()
    index = 0
    with open("1000NodesList.txt", "r") as f:
        for line in f:
            array.append(line)
            ip = array[index]
            slice_val = "albany_ccnS17_1"
            hostname = "slice_val"+"@"+"ip"
            username = raw_input('username: ')
            password = getpass.getpass('password: ')
            s.login(hostname , password)
            s.sendline('uptime')   # run a command
            s.prompt()             # match the prompt
            print(s.before)        # print everything before the prompt.
            with open('newfile.txt', 'a+') as f:
                f.write(s.prompt())
                f.write("\n")
            index+=1; 
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)