#python program to check the given number is in range or not


def check_range():
    a=int(input("enter the nummber "))
    r=int(input("enter the range (by default start is from 1) : "))
    for i in range(1,r+1):
        if a == i :
            print("present")
            break
        else:
            continue
    if(i==r):
        print("not present")
        

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")


check_range()

test_range(5)