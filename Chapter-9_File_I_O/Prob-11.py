# Rename a File to "renamed_by_python.txt"
with open("old.txt", "r") as f:
    v =  f.read()
with open("renamed_by_python.txt", "w") as f:
    f.write(v)

    print(f.tell())# Tell the position of the file
    f.seek(0) # U can go to 0th position of the file

    print(f.tell())

with open("Screenshot_20241108_130223.jpg","rb")as f: # rb for...?
    data = f.read()
    print(data)

with open("Screenshot_20241108_130223.jpg","wb")as d: # wb for ...?
    d.write(data)

print(dir(__builtins__)) # Make comma in each words