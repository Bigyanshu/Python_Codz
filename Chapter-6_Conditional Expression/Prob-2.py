# Entered 3 subjeects mark & min 40% is pass & less than33% is fail

mark1 = int(input("Enter mark: "))
mark2 = int(input("Enter Mark: "))
mark3 = int(input("Enter Mark: "))

total_Percent = (100*(mark1+mark2+mark3)/300)

if(total_Percent > 40 and mark1 >= 33 and mark2 >=33 and mark3 >=33):
    print("You are Pass",total_Percent)
else:
    print("You are Fail,Try Next Time",total_Percent)
