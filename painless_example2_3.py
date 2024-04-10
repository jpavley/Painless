# Painless Python
# A ridiculously deep dive into Python by way of the print function

# Example 2.2 solved the extra space and the number of arguments problems
# But we still have problems:
# - Every time the hello function runs we get the same result
# - If we want to say hello to someone else we have to change the hello function

# Let's see if we can make our script even less hard coded

# Example 2.3
# Passing an argument when a function is called

def main():
    hello_argument("George") # Pass the value of name when calling
    hello_argument("Susan")
    hello_argument("🤨")
    hello_argument("こんにちは")
    
def hello_argument(name: str): # give a parameter a type hint
    print(f"Hello, {name}!") # Use the parameter as a variable

# The hello_argument function can say hello to anyone!
# What does "name: str" mean?

if __name__ == "__main__":
    main()
