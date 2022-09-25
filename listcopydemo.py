l1 = [[1,2], [3,4]]

l2 = l1.copy() #shallow copy

print("L1:",l1)
print("L2:",l2)

l1[0][0]  =12

print("L1:",l1)
print("L2:",l2)

l1[0] = [4, 5]

print("L1:",l1)
print("L2:",l2)
