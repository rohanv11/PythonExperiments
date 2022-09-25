def square(x):
    for i in range(1, x+1):
        yield i ** 2

f = square(3)
print(next(f))
print(next(f))
print(next(f))

