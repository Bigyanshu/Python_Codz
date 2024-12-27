lst = [3,5,7,9,77,79,9,79,77,97]

def unique(li):
    new = []
    for i in li:
        if i not in new:
            new.append(i)
    print(new)

unique(lst)