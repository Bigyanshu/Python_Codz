with open("fileG.txt")as f:
    f.read()
with open("fileG.txt", 'w') as f:
    f.write("") # This empty string type makes fileG.txt is empty