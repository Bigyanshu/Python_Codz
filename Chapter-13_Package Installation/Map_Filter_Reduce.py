# Map
lst = [1, 2, 3, 4, 5, 6]

squares = lambda i: i*i
        # lambda 1: 1*1
        # lambda 2: 2*2

sqLst = map(squares, lst)
print (list(sqLst))


# Filter
lsts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
def even(x):
    if (x % 2 == 0):
        return True
    return False

onlyEven = filter(even, lsts)
print(list(onlyEven))


# Reduce
from functools import reduce
lyst = [1, 2, 3, 4]

def sum(a,b):
    return a+b
mul = lambda a ,b : a * b

print(reduce(sum,lyst))
print(reduce(mul,lyst))
