import sys, os, time
import paramiko
remote_path = "/tmp/"
tarnsport = paramiko.Transport(('192.168.226.131', 22))
tarnsport.connect(username='root', password='root')

sftp = paramiko.SFTPClient.from_transport(tarnsport)

sftp.put('wjx.py', os.path.join(remote_path, 'wjx.py'))

sftp.get('/tmp/wjx.py', 'wjx_01.py')
tarnsport.close()

print('DONE')
