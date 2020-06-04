import sys, os, time
import requests
import settings
import importlib


def get_server_info(hostname):
    import paramiko

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=22, username='root', password='root')
    stdin, stdout, stderr = ssh.exec_command('df -h')
    res, err = stdout.read(), stderr.read()

    result = res if res else err

    return result.decode('utf8')


def run():
    for key, path in settings.PLUGINS_PATH_DICT.items():
        module_path, class_name = path.rsplit('.', maxsplit=1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        plugin_obj = cls()
        info = plugin_obj.process()
        print(key, info)


if __name__ == '__main__':
    run()
