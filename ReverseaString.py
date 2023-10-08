# Function to reverse and display a string
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Input string
input_string = input("Enter a string: ")

# Reverse and display the string
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
