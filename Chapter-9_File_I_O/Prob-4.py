'''A file contains a word donkey multiple times. You need to write a preog which replace this word
with #### by updating same files'''

word = "Donkey"

with open('fileE.txt', 'r') as f:
    v = f.read()
    content = v.replace(word, '######')

with open('fileE.txt', 'w') as f:
    f.write(content)