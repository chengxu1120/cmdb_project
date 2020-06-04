import sys, os, time
from .base import BasePlugin

class NetworkPlugin(BasePlugin):

    def process(self,ssh,hostname):
        data = ssh(hostname,'ip a')
        return data