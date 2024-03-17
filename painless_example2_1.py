# Painless Python
# A ridiculously deep dive into the the print function

def main():
    helloVariable()
    
# One problems with example 1 is that the message is "hard coded"...
# Hard coding is the process of embedding data into the source code of a script.
# (Yech!)

# Example 2.1
# Printing a message to the terminal using a variable
def helloVariable():
    name = "John" # Declare a variable called "name" and assign it the value "John"
    print("Hello,", name, "!") # use the variable as 1 of 3 arugments passed to the print function

# What is a variable?
# What does "declare" mean?
# What does "assign" mean?
    
if __name__ == "__main__":
    main()