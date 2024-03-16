# Painless Python
# A ridiculously deep dive into the the print function

def main():
    hello1()
    hello2()
    hello3()
    message()
    
# One problems with example 1 is that the message is "hard coded"...

# Example 2.1
# Printing a message to the terminal using a variable
def hello1():
    name = "John" # Define a variable called "name" and assign it the value "John"
    print("Hello,", name, "!") # use the variable as one of the arugments passed to the print function

# Example 2.2
# Printing a message to the terminal using a variable and the f-string method
def hello2():
    name = "Paul"
    print(f"Hello, {name}!")

# Example 2.3
# Printing a message to the terminal using a variable and the format method
def hello3(name="George"):
    print("Hello, {}!".format(name))

# Example 2.4
# Printing a message to the terminal using two variables and the format method
def message(greeting="Goodbye", name="Ringo"):
    print("{}, {}!".format(greeting, name))
    
if __name__ == "__main__":
    main()
