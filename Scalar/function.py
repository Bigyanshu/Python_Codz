def add(a,b):
    return a + b

def subtract(a,b):
    return a - b
print(add(3,4))
print(subtract(5,4))

func = (lambda a,b : a + b)(7,9)
print(func)

x = 9
y = 7
lambda x,y :x if x > y else y

lst = [(3,7),(79,97),(9,13)]
lst.sort(key = lambda x : x[1])
print(lst)