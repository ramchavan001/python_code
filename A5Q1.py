#program to print maximum from three number



def max_number(a,b,c):
    if (a > b) and (a > c):
        print("maximum of three is: ",a)
    elif (b>a) and (b>c):
        print("maximum of three is : ",b)
    else:
        print("maximum of three is : ",c)

def using_list():
    print("another method to find maximum :--->  ")    

    list=[]
    n=int(input("enter the number of element you want to insert in list: "))
    for i in range(0,n):
        ele=int(input("enter the element: "))
        list.append(ele)
    print("maximum from list : ",max(list))    
    


a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
c=int(input("enter the third number : "))
max_number(a,b,c)

using_list()