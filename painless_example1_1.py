# Painless Python
# A ridiculously deep dive into Python by way of the the print function

# Example 1.1
# Sending a message to something somewhere somehow

# This is the Minimum Viable Python script

def main(): # Define a function named "main"
    print("Hello, World!") # Print an argument to the terminal

# What is a script?
# What is a comment?
# What is a function?
# What is a argument?
# What is a terminal?

# Use a conditional statement to perform a test when running this script
if __name__ == "__main__": # if name of the current module is "__main__"
    # The script is being run directly
    print(__name__) # should be "__main__"
    main() # Call the function named "main"
else:
    # The script is being imported by another script
    print(__name__) # should be "painless_example1"
    pass # Don't do anything

# What is a conditional statement?
# How do you run a python script?
# What does run directly mean?
# What does import mean?
# If we run this script again, what will happen?
