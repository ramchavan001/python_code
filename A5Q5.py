#program to find the factorial of a given number

def factorial_of_nummber():
    a=int(input("enter the number to calculate factorial :-> "))
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    
    print("factorial of ",a," is :",fact)
    
factorial_of_nummber()