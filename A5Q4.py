#python program to reverse a given string

def reverse_string():
    string=input("enter the string: ")
    a=len(string)
    print("reverse_string is: ",string[::-1])
    
    str=""
    print("another way of reversing the string: ")
    for i in string:
        str=i+str
    print("reversed string : ",str)
        
    
    

reverse_string()