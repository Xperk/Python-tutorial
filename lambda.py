def x(a, b): return a * b
print(x(5, 6))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
# mydoubler = lambda a : 2*a
mytripler = myfunc(3)
print(mydoubler(11)) 
print(mytripler(11))