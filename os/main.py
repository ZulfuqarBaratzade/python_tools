import os
#for list directory
def list_directory_contents(path="."):
    print("Contents of directory:")
    for item in os.listdir(path):
        print(item)
#for create directory
def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")
#delete directory
def delete_directory(directory_name):
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except OSError as e:
        print(f"Error deleting directory: {e}")


#main function
def main():
    print("1. List contents of current directory")
    print("2. Create a new directory")
    print("3. Delete a directory")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        list_directory_contents()
    elif choice == "2":
        directory_name = input("Enter the name of the directory to create: ")
        create_directory(directory_name)
    elif choice == "3":
        directory_name = input("Enter the name of the directory to delete: ")
        delete_directory(directory_name)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


