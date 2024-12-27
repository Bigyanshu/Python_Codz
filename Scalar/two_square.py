def intro( **kargs):
    for key, value in kargs.items():
        print(key,value, sep= " :| ")

intro(name = "Mahy", age = 24, hobbies = ["Meditation", "Coding", "Study"] )

print("Next Question:-->\n")
def mix(a, b, c, age = 24, *args, **kwargs):
    print(a, b, c)
    print(age)
    print(args)
    print(kwargs)

mix(3,7,9, 23, 79,97,39,37, name="Mahy", hobbies = "Meditation")