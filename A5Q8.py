#Program to return unique element from list into new list

def unique_list():
    list=[]
    n=int(input("enter the number of element you want to enter in list"))
    for i in range(0,n):
        ele=int(input("enter the element : "))
        list.append(ele)
        
    print("unique_list : ", [set(list)])
    
unique_list()