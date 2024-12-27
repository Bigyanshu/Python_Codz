def myFunction():
    print("Hello My FIles")

# if this name_main file imported from another file then if block not executed
if __name__ == "__main__":
    print("We are directly running this code")
    myFunction()
    print(__name__)