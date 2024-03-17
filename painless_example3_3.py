# Painless Python
# A ridiculously deep dive into the the print function
import painless_example2_4 as pe2

# Example 3.2
# Get input from the user

def main():
    greeting = input("What is your greeting? ")
    name = input("What is the name of the greeted? ")
    pe2.message(greeting=greeting, name=name)

# One thing that always confused me is that arugments can have the same name as parameters

if __name__ == "__main__":
    main()
    

name = input("What is your name? ")
pe2.message(greeting="Hi there my friend", name=name)
#print("Hello, " + name + "!")

# Example 3.2
# Printing a message to the terminal using the input function and concatenation
print("Hello, " + input("What is your middle name? ") + "!")

# Example 3.3
# Printing a message to the a file using the input function
print("Hello, " + input("What is your last name? ") + "!", file=open("output.txt", "a"))
