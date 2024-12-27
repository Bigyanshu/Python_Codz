'''WAP to print 3rd, 5th & 7th element from a list using enumerate function'''

lst = [3,5,7,9,73,37,97,77,79]

for index, item in enumerate(lst):
    if index == 2 or index == 4 or index == 6:
        print(item)