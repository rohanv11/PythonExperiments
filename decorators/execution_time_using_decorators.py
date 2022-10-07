import time
import math

def calculate_execution_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken by",func.__name__,":", end - start)
    return inner

#@calculate_execution_time
def factorial(num):
    time.sleep(2)
    print("Factorial:",math.factorial(num))

factorial = calculate_execution_time(factorial)



factorial(10) # ==> inner(10)