a = (1)
print(a)
print(type(a))

a = (1,)
print(a)
print(type(a))

a = (1,3,7,9,False,"Mahy","Omny")
print(a)
print(type(a))

# Tuple functions

print(len(a)) # Output: 7

# a[0] = 90 # TypeError: 'tuple' object does not support item assignment

no = a.count(False) 
print((no)) # Output:  1

i = a.index(False)
print((i)) # Output: 4

t = (1,2,35,67,9)
print(max(t)) # Output: 67
print(min(t)) # Output: 1
print(sum(t)) # Output: 114
print(sorted(t)) # Output : [1, 2, 9, 35, 67]
print(any(t)) # Output: True
print(all(t)) # Output: True

lst = [1,3,5,7,9]
t = tuple(lst)
print(t) # Output :(1, 3, 5, 7, 9)

# Unpacking a tuple in a list 
lst_t = [1,3,5,7,9]
a,b,c,d,e = lst_t
print("List:",lst_t)
print("List: A:",a)
print("List: B:",b)
print("List: C:",c)
print("List: D:",d)
print("List: E:",e)