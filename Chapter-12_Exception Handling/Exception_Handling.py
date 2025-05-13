try:
    # Code here
    a = int ( input ("Enter Anything but it is Integer : "))
    s = input("Enter Something but it is String By default: ")

    x = int ( input ("Enter a number: "))
    y = int ( input ("Enter another number: "))
    z = x/y
    print(z, type(z))
    print(a,type(a))
    print(s,type(s))
except ZeroDivisionError as z:
# except Exception as e:
    # print(e,type(e))
    print("Error is : ",z,type(z))
print("Thank you")


# except ValueError as v:
#     pass
# except TypeError as t:
#     pass
# except:
#     pass