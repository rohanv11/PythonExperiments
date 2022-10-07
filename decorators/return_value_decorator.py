def cal_sum_decorator(func):
    def inner(*args, **kwargs):
        print("BEFORE")
        returned_value = func(*args, **kwargs)
        print("AFTER")
        return returned_value
    return inner

@cal_sum_decorator
def sum(a, b):
    print("INSIDE FUNCTION")
    return a + b

print("Sum:", sum(10, 20))
