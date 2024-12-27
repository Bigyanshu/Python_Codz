'''WAP to read text from 'poem.txt' & findout wheather it contains 'twinkle' words'''

f =open('poem.txt', 'r')
v = f.read()
if("twinkle" in v):
    print("Yes, Present")
else:
    print("No, Absent")
f.close()
