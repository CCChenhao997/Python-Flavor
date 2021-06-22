'''
Description: 
version: 
Author: chenhao
Date: 2021-06-22 16:57:34
'''

def message(e):
    print(str(e))
    print(repr(e))
    exit()


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""
    def __init__(self, msg=None):
        super().__init__(self) #初始化父类
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return 'TimerError('+str(self.msg)+')'