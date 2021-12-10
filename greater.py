def g(a, b):
    if (b == 0):
        return a
    return g(b, a%b)


a = int(input("Eerste nummer "))
b = int(input("Tweede nummer "))
if(g(a, b)):
    print('De grootste gemeenschappelijke deler van', a, 'en', b, 'is', g(a, b))
