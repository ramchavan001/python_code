#program to check the given number is prime or not 

def check_prime(number):
    for i in range(2,number):
        if(number % i) == 0:
            print("not prime ")
            break
        if( i == number-1):
            print("given number is prime ")
        

number=int(input("enter the number for cheking whether it is prime or not "))
check_prime(number)