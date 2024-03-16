# Painless Python
# A ridiculously deep dive into the the print function

def main():
    helloVariable()
    
# One problems with example 1 is that the message is "hard coded"...
# Hard coding is the process of embedding data directly into the source code of a program.
# (Yech!)

# Example 2.1
# Printing a message to the terminal using a variable
def helloVariable():
    name = "John" # Define a variable called "name" and assign it the value "John"
    print("Hello,", name, "!") # use the variable as one of the arugments passed to the print function
    
if __name__ == "__main__":
    main()
