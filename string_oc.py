#program to find the number of occurances of character in string

a=input("enter the string :-> ")

print(dict((letter,a.count(letter)) for letter in set(a)))
