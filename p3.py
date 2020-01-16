import copy
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[15,16,17,18,19,20]

print("\nlist 1 :-> ",l1)
print("\nlist 2 :-> ",l2)
l3=l1 #shallow copy
#copy.copy() also used to perform shallow copy

print("\nlist 3 :-> ",l3)
print('\nID of List l1:', id(l1))
print('\nID of List l3:', id(l3))

#deep copy
l4=copy.deepcopy(l2)
print("\nlist 4:-> ",l4)
new_list=[21,22,23,24,25]
l4.append([21,22,23,24,25])
print("\nappended list l4:-> ",l4)
l3.extend([30,31,32,33,34,35])
print("\n extended list l3:-> ",l3)
print("\nremoved element from l3",l3.remove(33))
print("\npop method on l4 :-> ",l4.pop())
l4.insert(1,78)

print("insert at first index of l4 :-> ",l4) 




