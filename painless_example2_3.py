# Painless Python
# A ridiculously deep dive into the the print function

# Example 2.2 solved the extra space and the number of arguments problems
# But we still have a hard coding problem: every time the hello_fstring 
# function runs we get the same result.

# Let's see if we can make it even less hard coded

# Example 2.3
# Printing a message to the terminal passing a argument when the function is
# called

def main():
    hello_argument(name="George") # Set the value of name when calling
    
def hello_argument(name):
    print(f"Hello, {name}!") # Use the arguement as a variable

# The hello_argument function can say hello to anyone!

if __name__ == "__main__":
    main()
