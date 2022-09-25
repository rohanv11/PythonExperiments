"""
Decorators are a very powerful and useful tool in Python since it allows programmers to 
modify the behaviour of a function or class. Decorators allow us to wrap another function 
in order to extend the behaviour of the wrapped function, without permanently modifying it
"""

def decorator_func(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner


def f1():
    print("OYE, HIE")


function_to_be_used = decorator_func(f1)

function_to_be_used()
decorator_func(f1)()
