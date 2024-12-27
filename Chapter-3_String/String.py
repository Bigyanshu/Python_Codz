a = 'Mahy'          # '0,1,2,3' or Reverse is = "-4,-3,-2,-1"
b = "Mahi"          # '0,1,2,3' or Reverse is = "-4,-3,-2,-1"
c = '''Bigyanshu''' # '0,1,2,3,4,5,6,7,8' or Reverse is = "-9,-8,-7,-6,-5,-4,-3,-2,-1"

name = a[-1]
print(name)

name1 = b[0:3]  # In this type u can access index 0 to n-1 index
                # Means if u enter [0:3] = 0 to 2 index
print(name1)

name2 = len(c)
print("Length of c variable is :",name2)
name3 = c[8]
print(name3)
O = c[0:7]      # Slicing
print(O)
O1 = c[-9:-3]   # Negative Slicing 
print("O1 is:",O1)
O2 = c[:6]      # Starting index to 6-1 index
print("O2 is:", O2)

var = "Bigyandipty"    # '0,1,2,3,4,5,6,7,8,9,10' or Reverse is = "-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1"

# print(var[0:])       # Is same as print(var[0:11])
# print(var[:11])      # Is same as print(var[0:11])
print(var[-11:-1])       # 
print(var[-11:0])       # Empty
# print(var[-11:])     # Is same as print(var[0:11])
# print(var[:-1])      # Is same as print(var[0:10])||print(var[-11:-1]) & giving (len-1)
# print(var[:-0])      # Empty
# print(var[:])        # Is same as print(var[0:11])