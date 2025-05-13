a = 97
b =79
def fun():
    a = 3
    print(a)
fun()
print(a)

# Output: 3
#         97

def main():
    global b
    b = 7
    print(b)
main()
print(b)

# Output: 7
#         7
    