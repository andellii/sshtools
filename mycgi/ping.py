#!C:\Users\m.andrigym\AppData\Local\Programs\Python\Python39\python.exe
import paramiko
import sys
import codecs

def remote_host1():
    varHost = "103.130.199.35"
    varPort = "44449"
    varUser = "andeli"
    varPass = "Andri_890"
    command = "ping 8.8.8.8 -c 3"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(varHost, varPort, varUser, varPass)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.read()
    lines_str = lines.decode('UTF-8')
    return lines_str
lines_str = remote_host1()
print('''
<html>
<head>
<title> Output Ping </title>
<body>
Hello!! %s
</body>
</head>
</html>
''' % lines_str)
