#!/usr/bin/env python
import paramiko
import time
import os


host = "127.0.0.1"
port = 22
username = "admin"
password = "admin"
command = "/system identity print"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

	# Invoke Shell
remote_connection = ssh.invoke_shell()

time.sleep(5)
output = remote_connection.recv(10240)
	
print(output)

# Command String (Checks the Router Network Identity)
com1 = remote_connection.send("/system identity print\n")           

time.sleep(5)
output1 = remote_connection.recv(10240)

print(output1)

ssh.close()
