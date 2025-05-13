# Findout spam message or not 

p1 = "Make a lot of Money"
p2 = "Buy Now"
p3 = "Subscribe This"
p4 = "Click This"

msg = input("Enter Your Comment: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("The comment is Spam...!")
else:
    print("The comment is not Spam ")

#  Alternate way
p1 = 'Make a lot of money'
p2 = 'Buy Now'
p3 = 'Subscribe this'
p4 = 'Click this'

msg = input("Enter Your Message : ")

if((p1 in msg) | (p2 in msg) | (p3 in msg) | (p4 in msg)):
    print("It is a Hacker !, Keep away don't touch any Links")
else:
    print("Welcome, it is safe.")