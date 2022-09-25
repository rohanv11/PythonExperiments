s = "rohan prashant varadkar"

def UniqueChars(s):
    d = dict()
    new_s = ""
    for c in s:
        if c in d:
            pass
        else:
            d[c] = 1
            new_s = new_s + c
    print(new_s)

UniqueChars(s)
print("hi")