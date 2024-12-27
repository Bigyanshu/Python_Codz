with open("this.txt")as f:
    v = f.read()
with open("this_copy.txt", 'w') as f:
    f.write(v)