# 1
class Employee:
    name = 'Mahy' # These 3 are class attributes
    lang = 'Python'
    sal = 213000

bgu = Employee()
print(bgu.name,bgu.lang,bgu.sal)

# 2
class Employee:
    name = 'Mahy' # These 3 are class attributes
    lang = 'Python'
    sal = 213000

bgu = Employee()
bgu.name = 'Mahi' # These object / instance attributes & More priors than the class attributes
bgu.lang = 'React' # These object / instance attributes & More priors than the class attributes
bgu.sal = 300000 # These object / instance attributes & More priors than the class attributes
print(bgu.name,bgu.lang,bgu.sal)