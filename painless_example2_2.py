# Painless Python
# A ridiculously deep dive into the the print function

def main():
    hello_fstring()
    
# Example 2.1 started to sovle the hard coding problem
# But now we have this extra space between the name and the exclamation point
# Another problem is that we might run out of arguments to pass to the print 
# function (is there a limit? Who knows but probably!)

# Is there a way to merge the values of many variables into a single string?

# Example 2.2
# Printing a message to the terminal using a variable and the f-string 
# technique

def hello_fstring():
    name = "Paul" # Set the value of name before we call print
    print(f"Hello, {name}!") # Pass the variable as an arguement to print

# What is a string?
# What do the quoation marks do?
# What is a f-string?
# What does the f in front of the string do?
# What do the curly braces do?
# How many arguments are passed to the print function?
    
if __name__ == "__main__":
    main()
