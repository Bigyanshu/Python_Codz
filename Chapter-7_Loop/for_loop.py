# # Three types u can declare range function
# for i in range(10):
#     print(i)

# # for i in range[:10] :
# #     print(i)

# for i in range(0,10,2) :
#     print(i)

# List in for loop
l = [1,4,5,67,89,99]

for i in l:
    print("List is : ",i)
for i in l:
    if i%2 ==0:
        print("Even no's are: ",i)

# String in for loop
z = "Mahy's Omny Scent"

for  i in z:
    print("String is: ",i)

print(len(z))

# Tuples in for loop
t = (3,7,9,21,23,56,97)

for i in t:
    print("Tuple is:",i)
