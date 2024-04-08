# Painless Python
# A ridiculously deep dive into Python by way of the the print function

# Example 2.2 solved the extra space and the number of arguments problems
# But we still have problems:
# - Every time the hello function runs we get the same result
# - If we want to say hello to someone else we have to change the hello function

# Let's see if we can make our script even less hard coded

# Example 2.3
# Printing a message to the terminal passing a argument when the function is called

def main():
    hello_argument(name="George") # Set the value of name when calling
    hello_argument(name="Susan")
    hello_argument(name="🤨")
    hello_argument(name="こんにちは")
    
def hello_argument(name):
    print(f"Hello, {name}!") # Use the parameter as a variable

# The hello_argument function can say hello to anyone!

if __name__ == "__main__":
    main()
