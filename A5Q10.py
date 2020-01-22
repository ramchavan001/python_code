#program to print even number from the list

def print_even_num():
    list=[]
    even_list=[]
    n=int(input("enter the number of element for the list "))
    for i in range(0 , n):
        ele=int(input("enter the element "))
        list.append(ele)
        
    for i in list:
        if(i%2)==0:
            even_list.append(i)
    print("even number list : ",even_list)
    
print_even_num()
            
        