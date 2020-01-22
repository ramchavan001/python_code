#program to calculate number of uppercase and lowercase letter in basestring

def case_letter(string):
    upper_count=0
    lower_count=0
    for i in string:
        if(i.isupper()):
            upper_count=upper_count+1
        elif(i.islower()):
            lower_count=lower_count+1
            
    print("upper letter count: ",upper_count,"\n lower letter count : ",lower_count)
    

string=input("enter the string ")
case_letter(string)
            
    