import time
import threading
class Singleton(object):
    instance = None #静态字段、类变量
    lock = threading.RLock()
    def __init__(self,name):
        """
        初始化对象
        :param name:
        """
        self.name = name

    def __new__(cls, *args, **kwargs):
        """
        创建对象
        :param args:
        :param kwargs:
        :return:
        """
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                time.sleep(1)
                cls.instance = object.__new__(cls)
            return cls.instance


def func():

    obj1 = Singleton('alex')
    # obj2 = Singleton('alex')

    print(obj1)

for i in range(10):
    t = threading.Thread(target=func)
    t.start()