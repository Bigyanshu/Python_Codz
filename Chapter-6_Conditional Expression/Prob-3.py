p1 = "Make a lot of Money"
p2 = "Buy Now"
p3 = "Subscribe This"
p4 = "Click This"

msg = input("Enter Your Comment: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("The comment is Spam...!")
else:
    print("The comment is not Spam ")