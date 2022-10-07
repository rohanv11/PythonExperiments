def say_hi(name):
    return "HI! "+name



f1 = say_hi
print(f1("Rohan"),"Type of F1",type(f1))

f2 = say_hi("Danish")
print(f2, "Type of F2",type(f2))


def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
print(add_15(10), "Type of add_15", type(add_15))

