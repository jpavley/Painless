# Painless Python
# A ridiculously deep dive into the the print function

def main():
    hello_variable()
    
# One problem with example 1 is that the message is hard coded...
# Hard coding is inflexable, static, resistant to change

# Let's see if we can make it less hard coded

# Example 2.1
# Printing a message to the terminal using a variable

def hello_variable():
    name = "Angel" # Declare a variable assign it a value
    # Use the variable as 1 of 3 arugments passed to the print function
    print("Hello,", name, "!")

# What is a variable?
# What is a value?
# What does declare mean?
# What does assign mean?
    
if __name__ == "__main__":
    main()
