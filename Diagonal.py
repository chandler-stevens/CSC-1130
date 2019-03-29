# *---*
# **--*
# *-*-*
# *--**
# *---*

def diagonal(n):
    a = -1
    b = n-2
    for y in range(0,n):
        print("*", end="")
        for x in range(0,a):
            print("-", end="")
        if y != 0 and y != (n-1):
            print("*", end="")
        for x in range(0,b):
            print("-", end="")
        print("*")
        a += 1
        b -= 1

diagonal(5)
