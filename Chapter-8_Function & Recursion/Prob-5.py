# return statement go to next line 

def pattern(n):
    if n==0:
        return
    print('*'*n)
    print(n-1)
    
x = int(input('Enter a No.: '))
pattern(x)