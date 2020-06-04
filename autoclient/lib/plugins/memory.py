import sys, os, time
from .base import BasePlugin

class MemoryPlugin(BasePlugin):
    def process(self,ssh,hostname):
        data = ssh(hostname,'cat /proc/cpuinfo')
        return data