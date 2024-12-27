# read()

import os
print(os.path.exists("filer.txt"))

f = open("filer.txt")
data = f.read()
print (data)

# write()

s = 'Mahy You Are Becaming a Smart Girl'
f = open("fileC.txt", 'w')
f.write(s)

# readline() : It returns list formatted

f =open("fileD.txt")

lines = f.readlines()
print(lines, type(lines))

lines1 = f.readlines()
print(lines1, type(lines1))

lines2 = f.readlines()
print(lines2, type(lines2))

lines3 = f.readlines()
print(lines3, type(lines3))

lines4 = f.readlines()
print(lines4 =="") 
# If your file is not containing that no of lines then thorough Falses

lines5 = f.readlines()
print(lines5 == "")

# or

f =open("fileD.txt")
line = f.readline()
while(line != ""):
    print(line,type(line)) # Returns String (str) type
    line = f.readline()

# append()

st = " O Mahy Mahi Ve O Mahy O Mahy" # This lines are added fileB.txt files
f =open("fileB.txt","a")
f.write(st)

# rb(): Read in Binary Mode

# rt(): Read in Text Mode

# with statement()

with open('fileA.txt') as f :
    print(f.read())

f.close() # This lines close the files in system