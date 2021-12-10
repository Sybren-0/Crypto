import math
def checkpriem():
    i = input("Check of je nummer een priemgetal is: ")
    a = int(i)
    b = 2
    c = "Ja"
    while b < a:
        if a%b == 0:
            c = "Nee"
        b = b+1
    print(c)
checkpriem()

def checkdivisible():
    a = input("Check alle delers: ")
    b = []
    while b < a:
        if b % a == 0:
            b.append(a)
    print(b)
checkdivisible()