'''WAP to find max of num in a list using reduce function'''

from functools import reduce

lst = [3,77,9==9,7,739,97,99]
def greater(n, m):
    if n > m:
        return n
    return m
print(reduce(greater, lst))
