# WA function to remove given word from lstist ad strip it at same time
def rem_word(lst, word):
    n = []
    for item in lst:
        if not (item == word):
            n.append(item.strip(word))
    return n

lst = ["Mahy", "Bgu", "Omny", "Rohan", "an"]

print(rem_word(lst,"an"))
print(rem_word(lst,"y"))
print(rem_word(lst,"u"))