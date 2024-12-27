with open("this.txt")as f:
    v = f.read()
with open("this_copy.txt", 'w') as f:
    c = f.write(v)

if (v == c):  # if(c == v) return--> No, Not identical
    print("Yes, File is Identical")
else:
    print("No, File is not Identical")