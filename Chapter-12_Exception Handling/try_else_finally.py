# try with else & finally

# try with else:

try:
    x = int ( input ("Enter a number: "))
    y = int ( input ("Enter another number: "))
    z = x/y
    print(z, type(z))

except ZeroDivisionError as z:
    print("Error is : ",z,type(z))

except Exception as e:
    print(e,type(e))

except ValueError as v:
    print(v,type(v))

except TypeError as t:
    print(t,type(t))
else : #if try block succefully run then entering to else block
    print("No error occurred,\nI'm in else")

# try with finally:
def main():
    try:
        a = int ( input ("Enter a Number: "))
        print(a, type(a))
        return

    except Exception as e:
        print(e,type(e))
        return
    finally: 
# finally block always run if other part are successfully run or not
# It also run, if in function you return then final block override any class/method & run
        print("I'm in Finally")
main()