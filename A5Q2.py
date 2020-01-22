#program to print sum of all element in the list





def element_sum():

    list=[]
    n=int(input("enter the number of element you want to insert in list: "))
    for i in range(0,n):
        ele=int(input("enter the element: "))
        list.append(ele)
    print("sum : ",sum(list))  
    
    print("another method: ")
    tot=0
    for i in range(0,n+1):
         tot=tot+i
        
    print("sum ",tot)
    


element_sum()