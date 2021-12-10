def lowest():
    a = int(input("Eerste nummer "))
    b = int(input("Tweede nummer "))
    if a > b:
       c = a
    else:
       c = b

    while(1):
       if ((c % a == 0) and (c % b == 0)):
           d = c
           break
       c += 1
    return print("De kleinste gemeenschappelijke deler van ",a," en ",b," is ",d)


lowest()
