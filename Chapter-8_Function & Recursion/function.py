# 1
def goodDay(name):
    """
    This function prints a personalized greeting with the given name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    None: The function prints the greeting directly, so it does not return any value.
    """
    print("1-Good Day, "+ name)

goodDay("Mahy")
goodDay("Bgu")
goodDay("Omny")
goodDay("Mahi")

# Output:
'''
Good Day, Mahy
Good Day, Bgu
Good Day, Omny
Good Day, Mahi'''

# 2-Multiple Parameters
def goodDay(name, ending):
    print("2-Good Day, " + name + ending)
    # print("Good Day, " + name)
    # print(ending)

goodDay("Mahy", " Thanks")
goodDay("Bgu", " Thank you")
goodDay("Omny"," Nothing")
goodDay("Mahi", " Welcome")

# 3-return type function
def goodNight(name, ending):
    print("3-Dood,"+ name + ending)
    return "OK"

a = goodNight("Mahy"," omny")
print(a)

# 4- Default parameters
def goodBoy(name, ending = 'Thanks'):
    print(f"4-Good Boy, {name}")
    print(ending)
goodBoy("Bgu")
goodBoy("Mahi", "Mahi is Good girl not Boy")