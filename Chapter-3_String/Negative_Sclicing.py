c = '''Bigyanshu''' # '0,1,2,3,4,5,6,7,8' or Reverse is = "-9,-8,-7,-6,-5,-4,-3,-2,-1"

O = c[0:7] # Slicing
print(O)
O1 = c[-9:-3] # Negative Slicing 
print(O1)

var = "Bigyandipty"    # '0,1,2,3,4,5,6,7,8,9,10' or Reverse is = "-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1"

print(var[0:])       # Is same as print(var[0:11])
print(var[:11])      # Is same as print(var[0:11])
print(var[-11:-1])   # Is same as print(var[0:10]) & giving (len-1)

print(var[-11:0])    # Empty

print(var[-11:])     # Is same as print(var[0:11])
print(var[:-1])      # Is same as print(var[0:10])||print(var[-11:-1]) & giving (len-1)

print(var[:-0])      # Empty

print(var[:])        # Is same as print(var[0:11])

bgu = "Pragyandipti Bigyanshughg"
print(bgu[0:24:7])  
print(bgu[::7])  
