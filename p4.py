num1=int(input("enter first number "));
num2=int(input("enter second number"));

print("\nbinary of num1 :-> ",bin(num1));
print("\nbinary of num2 :-> ",bin(num2));

print("\nAND ",num1 and num2)
print("\nOR ",num1 or num2)
print("\n NOT ",not(num2))
print("\n XOR ",num1 ^ num2) #xor operation

if(num1==num2):
    print("\ntrue")
else:
    print("\nfalse")
    
if(num1!=num2):
    print("\ntrue")
else:
    print("\nfalse")

if(num1>=num2):
    print("\ntrue")
else:
    print("\nfalse")

if(num1<=num2):
    print("\ntrue")
else:
    print("\nfalse")

if(num1>num2):
    print("\ntrue")
else:
    print("\nfalse")

if(num1<num2):
    print("\ntrue")
else:
    print("\nfalse")
    

print("\nleft shift of num1 by 4 :-> ",num1<<4)
print("\nright shifting of num2 by 3 :-> ",num2>>3)