import copy

l1 = [[1,2], [3,4]]
l2 = copy.copy(l1)

l1.append(1)

print("L1:",l1)
print("L2:",l2)

l1[1][0] = 23

print("L1:",l1)
print("L2:",l2)

# in shallow copy new object is created, but the refernces of old object are copied

#raise TypeError("hi")