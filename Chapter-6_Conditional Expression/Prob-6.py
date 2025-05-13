# Calculate grade to his Mark

mark = int(input("Enter Sub Mark: "))

# Grade system

if (mark <= 100 and mark >= 90):
    grade = "O"
elif (mark < 90 and mark >= 80):
    grade = "A"
elif (mark < 80 and mark >= 70):
    grade = "B"
elif(mark < 70 and mark >= 60):
    grade = "C"
elif(mark < 60 and mark >=50):
    grade = "D"
else:
    grade = "F"
    print("You are Fail",grade)
    
print("Your Grade is : ",grade)