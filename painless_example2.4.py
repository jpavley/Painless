# Painless Python
# A ridiculously deep dive into the the print function

def main():
    message(greeting ="Yo", name="Ringo")
    
# Example 2.3 is much less hard coded than before for still contains hard coding.

# Example 2.4
# Printing a message to the terminal using two variables inside an f-string
def message(greeting, name):
    print(f"{greeting}, {name}!")
    
# One thing that is cool is we wrapped the print function in a function called "message".
# This if we find something better than the print function we can change without changing 
# the rest of our code.
    
# What else can we do with the with our message function?
# - Change the greeting based on the time of day?
# - Get input from the user?
# - Print to a file?
# - Reuse the message function in another script?
# - Can we find a better way to "print" to the terminal and to files?
    
if __name__ == "__main__":
    main()
