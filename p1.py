

f_name=input("enter First Name: ")
l_name=input("enter Last Name: ")
age=int(input("enter Age: "))
salary=int(input("enter salary : "))

print("\n First Name :-> ",f_name)
print("\n Last Name :-> ",l_name)
print("\n Age :-> ",age)
print("\n Salary :-> ",salary)

print("\n String Concatenation :-> ", f_name + l_name)
a=f_name[3:-3]
print("\n",a)

print("\n binary of age :->" ,bin(age))
print("\n binary of salary :->" ,bin(salary))

print(type(f_name))
print(type(l_name))
print(type(age))
print(type(salary))

print(ord(f_name[0]))
print(ord(l_name[0]))
