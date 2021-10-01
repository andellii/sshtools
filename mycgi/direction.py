#!C:\Users\m.andrigym\AppData\Local\Programs\Python\Python39\python.exe

import cgi
import cgitb
import paramiko
cgitb.enable()

form = cgi.FieldStorage()
# Get data from fields
def myCond():
   if (form.getvalue('subject') == 'option1'):
      choice = 'This is Option 1'
   elif (form.getvalue('subject') == 'option2'):
      choice = 'This is Option 2'
   else:
      choice = 'Not Choice anything'
   return choice
myCond_result = myCond()

def host1():
   varHost = "103.130.199.35"
   varPort = 44449
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

def host2():
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

def final():
   if (myCond_result == 'This is Option 1'):
      final_opt = host1()
   elif (myCond_result == 'This is Option 2'):
      final_opt = host1()
   else:
      final_opt = 'Blank'
   return final_opt
final_opt = final()

print("Content-Type: text/html")
print('''
<html>
<head>
<title> %s </title>
<body>
Hello!! <br><br>%s
</body>
</head>
</html>
''' % (myCond_result, final_opt))