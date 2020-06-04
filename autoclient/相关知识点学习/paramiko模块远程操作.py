import  paramiko

#创建ssh对象
ssh = paramiko.SSHClient()

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='192.168.6.142', port=22, username='root', password='root')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -h')
# 获取命令结果
res, err = stdout.read().decode('utf8'), stderr.read().decode('utf8')

result = res if res else err

# 关闭连接
ssh.close()
print(result)