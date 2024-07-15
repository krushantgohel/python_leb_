# Initialize an empty list to store employee names
EMPNAME = []

# Function to add a name to the list
def add_employee(name):
    EMPNAME.append(name)
    print(f"{name} added to the list.")

# Function to remove a name from the list
def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"{name} removed from the list.")
    else:
        print(f"{name} not found in the list.")

# Function to append a name to the list
def append_employee(name):
    EMPNAME.append(name)
    print(f"{name} appended to the list.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nCurrent Employee List:", EMPNAME)
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Append Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter the employee name to add: ")
            add_employee(name)
        elif choice == '2':
            name = input("Enter the employee name to remove: ")
            remove_employee(name)
        elif choice == '3':
            name = input("Enter the employee name to append: ")
            append_employee(name)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
