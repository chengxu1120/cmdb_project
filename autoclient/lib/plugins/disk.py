import sys, os, time
import settings
from .base import BasePlugin


class DiskPlugin(BasePlugin):
    def process(self, ssh,hostname):
        data = ssh(hostname, 'df -h')
        return data
