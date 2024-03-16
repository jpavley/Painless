# Painless Python
# A ridiculously deep dive into the the print function

def main():
    helloFString()
    
# Example 2.1 kinda sovled hard coding problem.
# But now we have this extra space between the name and the exclamation point.
# Another problem is that we might run out of arguments to pass to the print function.

# Example 2.2
# Printing a message to the terminal using a variable and the f-string method
def helloFString():
    name = "Paul"
    print(f"Hello, {name}!")

# What is a f-string?
# What do the curly braces do?
# How many arguments are passed to the print function?

# Example 2.2 solved the extra space and the number of arguments problems.
# But we still have the hard coding problem.

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
