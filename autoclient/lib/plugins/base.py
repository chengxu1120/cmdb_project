import sys, os, time

class BasePlugin(object):
    """
    基类，用于做约束，约束子类必须要实现的方法
    """
    def process(self,ssh,hostname):
        raise NotImplementedError('%s process must be overridden.'%self.__class__.__name__)