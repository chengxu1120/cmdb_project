import sys, os, time
import paramiko
import settings
import importlib
def get_server_info(ssh,hostname):
    server_info = {}
    for key, path in settings.PLUGINS_PATH_DICT.items():
        module_path, class_name = path.rsplit('.', maxsplit=1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        plugin_obj = cls()
        info = plugin_obj.process(ssh,hostname)
        server_info[key] = info

    return server_info