#WAPP which takes two set as inout and perform the operation same as in list example
import copy
s1={1,2,3,4,5,6,7,8,9,10}
s2={15,16,17,18,19,20}

print("\nset 1 :-> ",s1)
print("\nset 2 :-> ",s2)
s3=s1 #shallow copy
#copy.copy() also used to perform shallow copy

print("\nset 3 :-> ",s3)
print('\nID of set l1:', id(s1))
print('\nID of set l3:', id(s3))

#deep copy
s4=copy.deepcopy(s2)
print("\nset 4:-> ",s4)

new_set=(21,22,23,24,25)
s4.add(new_set)
print("\nappended set s4:-> ",s4)
#s3.extend({30,31,32,33,34,35})
#print("\n extended set s3:-> ",s3)
s3.remove(5)
print("\nafter removing element from s3",s3)
print("\npop method on s4 :-> ",s4.pop())
#s4.insert(1,78)

#print("\n insert at first index of s4 :-> ",s4) 
some_data = [1, 2, 4, 1, 6, 23, 3, 56, 6, 2, 3, 5, 6, 32, 2, 12, 5, 3, 2]
n = {x for i, x in enumerate(set(some_data)) if i < 5}
print(n) 

#slicing in list
#slice_obj=slice(4,7)
#print("sliced set s3 :-> ",s3({slice_obj}))
