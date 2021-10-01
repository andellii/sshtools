#!C:\Users\m.andrigym\AppData\Local\Programs\Python\Python39\python.exe

import cgi
import paramiko
import cgitb
cgitb.enable()
# Get data from fields HTML

def host1():
   varHost = "103.167.170.254"
   varPort = 8686
   varUser = "cantik"
   varPass = "banten2006"
   command = "ping 8.8.8.8 count=3"
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(varHost, varPort, varUser, varPass)
   stdin, stdout, stderr = ssh.exec_command(command)
   lines = stdout.read()
   lines_str = lines.decode('UTF-8')
   return lines_str
results = host1()

print("Content-Type: text/html")
print('''
<html>
<head>
<title> Title </title>
<body>
Hello!! <br><br>%s
</body>
</head>
</html>
''' % results)