def f1():
    yield 1
    yield 2
    yield 3

print("HI", next(f1()))
print("HI", next(f1()))
print("HI", next(f1()))

for val in f1():
    print(val)

generator_obj = f1()
print("Generator_obj type:",type(generator_obj))
print("f1() type:",type(f1()))
print("HI", next(generator_obj))
print("HI", next(generator_obj))
print("HI", next(generator_obj))
#print("HI", next(generator_obj))