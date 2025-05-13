'''WAP to open three files 1.txt, 2.txt and 3.txt, if any these file are not
present, a msg without exiting programm must be printed promting same.'''

try:
    with open("1.txt")as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open('3.txt')as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank You")