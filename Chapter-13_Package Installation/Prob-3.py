'''A list contains multiplication table of 7. WAP to convert it 
to a vertical string'''

table = [str(7 * i) for i in range(1,11)]

s = "\n".join(table)
print((s))
print(type(s))