import copy

l1 = [[1,2], [3,4]]
l2 = copy.deepcopy(l1)

l1.append(1)

print("L1:",l1)
print("L2:",l2)

l1[1][0] = 23

print("L1:",l1)
print("L2:",l2)

# in deep copy, all the item, nested items are copied recursively to the new object 
# (not just the references, new references are created)