a = "Mahy"
b = " bgyanshu prag "
ba = "Bgu Hello"

print(len(a))
print(len("ABCDE"))

print(a.endswith("hy")) # It validate String start with given input or not if correct then give True else False
print(a.endswith("Hy"))
print("ABD".endswith("aDB"))

print(a.startswith("Ma")) # It validate String start with given input or not if correct then give True else False
print(a.startswith("ma"))
print("MAHY".startswith("ma"))

print(b.capitalize()) # It only capitalise only 1st character not after space

print(b.upper())
print("bgyansu".upper())

print(b.lower())
print("PuCHky".lower())

print(b.strip())
print(" Bgyansu ".strip()) # This function eliminate starting & end whitespaces

print(ba.replace("Bgu","Bgyans"))
print("Mahy Bgu".replace("Bgu","Mahi"))

print(b.split()) # It separate strings after space
print("Bgu Mahy".split()) #['Bgu', 'Mahy']
print("Bgu" "Mahy".split()) #['BguMahy']
print("Bgu" ,"Mahy Bgu".split()) #Bgu ['Mahy', 'Bgu']

print(b.title()) # It Capitalize Each starting character
print('mahy bgu mahi'.title())

print("b".join(["Mix", "world"]))  # Output: 
print("b".join(["Mix"]))  # Output: Mix
print(b.join(["Mix"]))  # Output: Mix
print(b.join(["Mr&Mrs", "Panda"]))    # Output: 
print("".join(["hello", "world"]))   # Output: "hello-world"

print(b.find('ra')) # Output: 11 
print('Bigyanshu Puchky'.find(' ')) # Output:7
print('Bigyanshu Puchky'.find('Pu')) # Output:10
print('Bigyanshu Puchky'.find('Pragyan')) #If enter Wrong find then get '-1' as result

# print(.count())   This will give error as.count() is a method of string not integer
print(b.count('p'))
print('Mahhi Mahy'.count('h')) # Output: 3
print('Mahhi Mahy'.count('m')) # Output: 0

print('Hey {}'.format('Mahy')) # Output: Hey Mahy
print('Hey,{}'.format('Mahy')) # Output: Hey,Mahy

loo='1290'
print('12345'.isnumeric())
print(loo.isnumeric())
