from math import *
def Delers():
    a = int(input("Van welk nummer wil je de delers?:"))
    b = 1
    c = []
    while b < a:
	    if a % b == 0:
		    c.append(b)
	    b += 1
    for b in range(int(sqrt(a)), 0):
	    if a % b == 0:
		    c.append(a // b)
    c.append(a)
    print(c)
Delers()

# This code is contributed by himanshu77


            