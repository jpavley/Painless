# Painless Python
# A ridiculously deep dive into the the print function
import painless_example2 as pe2

# Example 3.1
# Printing a message to the terminal using the input function
name = input("What is your name? ")
pe2.message(greeting="Hi there my friend", name=name)
#print("Hello, " + name + "!")

# Example 3.2
# Printing a message to the terminal using the input function and concatenation
print("Hello, " + input("What is your middle name? ") + "!")

# Example 3.3
# Printing a message to the a file using the input function
print("Hello, " + input("What is your last name? ") + "!", file=open("output.txt", "a"))