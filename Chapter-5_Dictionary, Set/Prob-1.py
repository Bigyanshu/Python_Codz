""" Write a program to create a dictionary of Hindi words with values as their English
 translation. Provide user with an option to look it up!"""

words = {
    "Madad": "Help",
    "Omnipotent": "Bigyanshu",
    "Kela" : "Banana",
    "Billie": "Cat"
}
word = input("Enter a Hindi word to Translate in English: ")
print(words[word])