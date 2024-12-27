# Find out given post is taking about any thing or not...

post = input('Enter post: ')

# List of keywords that might be related to any topic
if("Mahy" in post.lower()):
# if("Mahy" in post):
    print("This post is discussing Mahy.")
else:
    print("This post is not discussing Mahy.")

# Why Error

l = [1,4,6,234,768]

for i in l:
    if(i%2 == 0 ):
        print(i)

z = "Mahy's Omny"
for i in z:
    print(i)