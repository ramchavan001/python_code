#program to calculate volume of sphere

import math
r=int(input("enter the radius of sphere: -> "))
cube=r*r*r
vol=math.floor((4/3)*math.pi*cube)
#pi=math.pi

print("volume of sphere:-> ",vol)