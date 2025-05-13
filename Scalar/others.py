# Which characters are repeated those are increasing

name = "Bigyanshu Sekhar Panda"

freq = {}
for i in name :
    if i not in freq :
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)