'''
Description: 
version: 
Author: chenhao
Date: 2021-06-22 16:43:19
'''


"""Context Manager"""
class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Hello, {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"See you later, {self.name}")


if __name__ == '__main__':
    with Greeter("Nick") as grt:
        print(f"{grt.name} is doing stuff...")