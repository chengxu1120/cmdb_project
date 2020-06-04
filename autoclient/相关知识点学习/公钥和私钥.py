import sys, os, time
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('c:\\Users\\Administrator.User-2019XXLQQY\\.ssh\\id_rsa')
# 创建ssh对象
ssh = paramiko.SSHClient()
# 允许连接不在know——hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='cmdb-centos7',port=22,username='root',pkey=private_key)

stdin,stdout,stderr = ssh.exec_command('df -h')

res,err = stdout.read().decode('utf8'),stderr.read().decode('utf8')

result = res if res else err

print(result)

ssh.close()