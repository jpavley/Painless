# Painless Python
# A ridiculously deep dive into Python by way of the the print function

def main():
    hello_variable()
    
# One problem with example 1.1 is that the message is hard coded...
# Hard coded means the code has to be rewritten to make an expected change
# Hard coding is inflexible, static, difficult to change
# Hard coding makes our code less reusable

# Let's see if we can make our script less hard coded

# Example 2.1
# Printing a message to the terminal using a variable

def hello_variable():
    name = "Angel" # Declare a variable assign it a value
    # Use the variable as a parameter passed to the print function as one of the arguments
    print("Hello,", name, "!")

    # Change the value of "name" and say hello to someone else...
    name = "Helen"
    print("Hello,", name, "!")

# What is a variable?
# What is a value?
# How do we declare a variable and assign it a value?
# What is a parameter?

if __name__ == "__main__":
    main()

# Don't need the "else:" part of the coditional statement because we were just going to "pass" anyway
