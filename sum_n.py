#WAPP which takes an integer as input and performs the sume operation , if enterd input is 0 or negetive number then break the programm
n=int(input("enter a number : "))
i=0
sum=0
if(n<=0):
    print("invalid number. ")
    #break
else:
    for i in range(1, n+1):
        sum+=i
print("sum : ",sum)
