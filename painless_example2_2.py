# Painless Python
# A ridiculously deep dive into the the print function

def main():
    helloFString()
    
# Example 2.1 kinda sovled hard coding problem.
# But now we have this extra space between the name and the exclamation point.
# Another problem is that we might run out of arguments to pass to the print function.

# Is there a way to include the values of many variables in a single string?
# (The official term for what we are trying to do is a "string interpolation")

# Example 2.2
# Printing a message to the terminal using a variable and the f-string method
def helloFString():
    name = "Paul"
    print(f"Hello, {name}!")

# What is a string?
# What is a f-string?
# What do the curly braces do?
# How many arguments are passed to the print function?
    
if __name__ == "__main__":
    main()
