from lib.plugins import get_server_info
from concurrent.futures import ThreadPoolExecutor
import time

def task(host):

    server_info = get_server_info(ssh, host)
    for key, value in server_info.items():
        print("============", key, "=============")
        print(value)
    # print(server_info)

def ssh(hostname,cmd):
    import paramiko

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=22, username='root', password='root')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    res, err = stdout.read(), stderr.read()

    result = res if res else err

    return result.decode('utf8')

def run():
    pool = ThreadPoolExecutor(2)
    host_list = ['192.168.226.131',
                 '192.168.226.131',
                 '192.168.226.131',
                 '192.168.226.131',
                 '192.168.226.131']
    for host in host_list:
        print('---------------',time.time())
        pool.submit(task,host)

if __name__ == '__main__':
    run()
