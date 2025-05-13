# Farehnite to celcius in function
def far_to_Cel(f):
    return 5 * (f-32)/9
f = int(input("Enter Temperature in Farehnite: "))

# print(far_to_Cel(f))
c = far_to_Cel(f)
print(f"{round(c,2)} degree c")