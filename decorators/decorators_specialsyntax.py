#By definition, a decorator is a function that takes another function and extends 
#the behavior of the latter function without explicitly modifying it.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func() #say_whee
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

#this below line gets executed using the '@my_decorator' syntax behind the scenes
#say_whee = my_decorator(say_whee)

say_whee()
print("Name of the func say_whee():", say_whee.__name__)
#Name of the func say_whee(): wrapper