# Painless Python
# A ridiculously deep dive into Python by way of the print function

def main():
    hello_fstring()
    
# Example 2.1 started to solve the hard coding problem
# But we have some problems...
# - We have this extra space between the name and the exclamation point--that was unexpected
# - We're passing 3 arguments to the print function: is there a limit? Who knows but probably!

# Is there a way to merge the values of many variables into a single string?

# Example 2.2
# Printing a message to the terminal using a variable and the f-string technique

def hello_fstring():
    name = "Nancy" # Set the value of name as we did before
    print(f"Hello, {name}!") # Use the f-string to embed the value of "name" into a single argument

    # Change the value of name and say hello to someone else
    name = "John"
    print(f"Hello, {name}!")

    # Can a string include an emoji?
    name = "🤨"
    print(f"Hello, {name}!")

    # Can a string include Japanese characters?
    name = "こんにちは"
    print(f"Hello, {name}!")

# What is a string?
# How can a string support English, emoji, and Japanese characters?
# What do the quotation marks do?
# What is a f-string?
# What do the curly braces do?
    
if __name__ == "__main__":
    main()
