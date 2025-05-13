''' File Management Project'''
import os

def create_File(filename):
    try:
        # File open & close with 'with' method
        with open(filename,'x') as f :
            # 'x' creating a new file 
            print(f"File Name {filename} : Created Successfully...!\n")
    # if file exist then this error will arise
    except FileExistsError:
        print(f"File Name {filename} already exist, you can't create same name file.\n")

    except Exception as E :
        print(F"An error occured :{E}\n")

# View All files
def view_all_Files():
    # this 'os.listdir' listing/Providing all files in current directory
    files = os.listdir() 
    if not files:
        print('File Not Found...!\n')
    else:
        print("File founded in Directory\n")
        # if file found that will show here
        for file in files:
            print(file)

# Delete Files
def delete_files(filename):
    try:
        os.remove(filename) #it will remove your file from your system
        print(F"{filename} deleted successfully...!\n")

    # if file not found this exceptioin will call
    except FileNotFoundError:
        print('File Not Found\n')
    # Some unkown or basic error this will call
    except Exception as E:
        print(f"An unknown error occured : {E}\n")

# For reading File
def to_read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(F"Content of {filename}: \n({content})") # showing content
    except FileNotFoundError:
        print(F"{filename} doesn't exist...!\n")

    except Exception as E:
        print(f"An error occured : {E}\n")

# Edit files
def edit_file(filename):
    try:
        with open(filename, 'a')as f:
            content = input("Enter data to add : ")
            f.write(content + "\n")
            print(f"Content added to {filename} Successfully.\n")
    except FileNotFoundError:
        print(F"{filename} doesn't exist...!\n")

    except Exception as E:
        print(f"An error occured : {E}\n")
# Main working file
def main():
    while True:
        print("\n---FILE MANAGEMENT APP---\n")

        print('1 : Create File')
        print('2 : View All File')
        print('3 : Delete File')
        print('4 : Read File')
        print('5 : Edit File')
        print('6 : Exit\n')

        # Select a no to doing operation
        choice = input("Enter your choice in No.(1-6) : ")

        if choice == '1':
            filename = input("Enter file name to create : ")
            create_File(filename)

        elif choice == '2':
            view_all_Files()

        elif choice == '3':
            filename = input("Enter File Name to Delete : ")
            delete_files(filename)
        
        elif choice == '4':
            filename = input("Enter File Name to Read : ")
            to_read_file(filename)

        elif choice == '5':
            filename = input("Enter your filename to Edit :")
            edit_file(filename)
        
        elif choice == '6':
            print("Closing the App...")
            break

        else:
            print("Invalid Choise")

if __name__ == '__main__':
    main()      