import sys, os, time
import requests

def get_server_info(hostname):
    import paramiko

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=22,username='root',password='root')
    stdin,stdout,stderr = ssh.exec_command('df -h')
    res,err = stdout.read(),stderr.read()

    result = res if res else err

    return result.decode('utf8')

def run():
    # 获取服务器信息
    info = get_server_info('192.168.226.131')
    print('连接服务器获取资产信息：',info)
    #http://127.0.0.1:8080/api/get_data/
    #get
    # result = requests.get(
    #     url='http://127.0.0.1:8080/api/get_data/',
    #     params={'host':'192.168.226.131','info':info}
    # )
    #post
    result = requests.post(
        url='http://127.0.0.1:8080/api/get_data/',
        data={'host': '192.168.226.131', 'info': info}
    )
    print('把资产信息发送给API：',result.text)

if __name__ == '__main__':
    run()