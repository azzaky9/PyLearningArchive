import math

def my_decorator(func):
    print("Before function called")
    func()
    print("after function called")

@my_decorator
def say_hello():
    print("Hello")


def multiply(func):
    print("before loop 10")
    func()
    print("process done.")

@multiply
def calc():
    for i in range(10):
        print(i)

calc()

