#Task 1: Input Length Validator
# Function to check name length
def check_name_length(name, name_type):
    if len(name) < 2:
        print(f"Error: The {name_type} must be at least 2 characters long.")
        return False
    return True

# Ask for first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Check the length of both names
if check_name_length(first_name, "first name") and check_name_length(last_name, "last name"):
    print(f"Hello, {first_name} {last_name}!")
