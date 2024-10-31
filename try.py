# Task 1: 
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Task 2: 
def access_element_at_index(input_list):
    try:
        index = int(input("Enter the index to access: "))
        value = input_list[index]
        print("Value at index", index, ":", value)

    except IndexError:
        print("Error: Index out of range.")

# Task 3: 
def read_file_contents():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File contents:\n", content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    else:
        print("File successfully opened.")

# Task 4: 
def write_to_file(data):
    try:
        with open("output.txt", 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")
    finally:
        print("File closed successfully.")

# Example Usage
divide_numbers()

example_list = [1, 2, 3, 4, 5]
access_element_at_index(example_list)

read_file_contents()

data_to_write = "Hello, this is some data to write to the file."
write_to_file(data_to_write)
