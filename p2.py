
str1=input("enter first String -> ")
str2=input("enter second String -> ")

print("\nFirst String :-> ",str1)
print("\nSecond String :-> ",str2)

str3=str1 + " " + str2

print("\nconcatenated new String third str3 :->",str3)
print("\nupper case of str3 :->",str3.upper())
print("\nlower case of str3 :->",str3.lower())
print("\ntitle case of str3 :->",str3.title())
splited_string=str1.split()
print("\nafter spliting join oepration: ",str3.join(splited_string))
print(" in center 30 spaces padding with $ ")
print(str3.center(30,"$"))


