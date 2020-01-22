#program to print multiplication of all element in the list

def element_mul():
    mul=1
    list=[]
    n=int(input("enter the number of element you want to insert in list: "))
    for i in range(0,n):
        ele=int(input("enter the element: "))
        list.append(ele)
        
    #print("multiplication: ")
    for i in list:
        mul=mul*i
    print("multiplication: ",mul)


element_mul()