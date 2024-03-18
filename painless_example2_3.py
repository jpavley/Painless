# Painless Python
# A ridiculously deep dive into the the print function

def main():
    helloArgument(name="George")
    
# Example 2.2 solved the extra space and the number of arguments problems.
# But we still have the hard coding problem.

# Let's see if we can make it even less hard coded.

# Example 2.3
# Printing a message to the terminal using a argument
def helloArgument(name):
    print(f"Hello, {name}!")

# Where did the value of the variable "name" come from?

if __name__ == "__main__":
    main()
