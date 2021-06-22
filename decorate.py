'''
Description: 
version: 
Author: chenhao
Date: 2021-06-22 16:58:52
'''

import time
import functools
from reader import feed
from timer import Timer


"""A standard decorator"""
def decorator(func):
    
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    
    return wrapper_decorator


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.4f} seconds.")
        return value
    return wrapper_timer


@timer
def test1():
    tutorial = feed.get_article(0)
    # print(tutorial)

@Timer(text="Downloaded the tutorial in {:.2f} s")
def test2():
    tutorial = feed.get_article(0)
    # print(tutorial)


if __name__ == '__main__':
    # test1()
    test2()