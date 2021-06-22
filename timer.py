'''
Description: 
version: 
Author: chenhao
Date: 2021-06-22 11:38:01
Reference: https://www.pythonf.cn/read/57854
'''
import time
import functools
from reader import feed     # pip install realpython-reader
from logger import logger
from contextlib import ContextDecorator
from exception import TimerError, message


"""A Python Timer Context Manager"""
class Timer(ContextDecorator):
    
    timers = dict()
    
    def __init__(self, name=None, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.name = name
        self.text = text
        self.logger = logger
        
        if name:
            self.timers.setdefault(name, 0)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
    
    def start(self):
        if self._start_time:
            # raise TimeoutError("Timer is running.")
            try:
                raise TimerError("Timer is running.")
            except TimerError as e:
                message(e)
                
        self._start_time = time.perf_counter()
    
    def stop(self):
        if not self._start_time:
            # raise TimeoutError("Timer is not running.")
            try:
                raise TimerError("Timer is not running.")
            except TimerError as e:
                message(e)

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
            
        if self.name:
            self.timers[self.name] += elapsed_time
            
        return elapsed_time
    
    def __call__(self, func):
        """
        If the Timer class inherits ContextDecorator, 
        the __call__ function is not needed.
        """
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper_timer
        

"""Instantiate the Timer class"""
def main1():
    name="download"
    t = Timer(name, logger=None)
    for tutorial_num in range(10):
        t.start()
        tutorial = feed.get_article(tutorial_num)
        t.stop()
        # print(tutorial)
        download_time = Timer.timers[name]
        
    logger.debug(f"Downloaded 10 tutorials in {download_time:.2f} seconds")


"""Use context manager"""
def main2():
    with Timer(logger=logger.debug):
        tutorial = feed.get_article(0)
        print(tutorial)

"""Use decorator"""
@Timer(logger=logger.debug)
def main3():
    tutorial = feed.get_article(0)
    print(tutorial)


if __name__ == '__main__':
    # main1()
    # main2()
    main3()