# Repeat Prog 4 for a list of such words to be censored.

words_to_censor = ['Donkey', 'Monkey','Hinkey']

with open('fileF.txt') as f:
    v = f.read()
for words in words_to_censor:
    content = v.replace(words, "#" * len(words))
    # It can change ur length means last word of ur list

with open('fileF.txt', 'w') as f:
    f.write(content)

# Exception Handling Methods

'''words_to_censor = ['Donkey', 'Monkey', 'Hinkey']

try:
    with open('fileF.txt', 'r') as f:
        content = f.read()

    for word in words_to_censor:
        content = content.replace(word, '#' * len(word))

    with open('fileF.txt', 'w') as f:
        f.write(content)

except FileNotFoundError:
    print("The file 'fileF.txt' does not exist.")
except IOError:
    print("An error occurred while reading or writing to the file.")'''