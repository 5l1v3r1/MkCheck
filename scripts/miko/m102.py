#!/usr/bin/env python
import paramiko
import time
import os

host = "127.0.0.1"
port = 22
username = "admin"  # CHANGE THIS
password = "admin"  # CHANGE THIS
apname = "/system identity print" # Change this for a different command to be run

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect(host, port, username, password)

remote_connection = p.invoke_shell()
time.sleep(5)
output = remote_connection.recv(2048)
print(output)

stdin, stdout, stderr = p.exec_command(apname)
opt = stdout.readlines()
opt = "".join(opt)
print(opt)
# print('opt' + line.strip('\n'))


p.close()

#####################################################______________ czFsM250NzggX18gUmFiYjE3J3MgRGVu ______________#####################################################
