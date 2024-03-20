# Painless Python
# A ridiculously deep dive into the the print function
import painless_example2_4 as pe2

# Example 3.2
# Get input from the user

def main():
    # Two ways to call the message function with user input:
    
    # 1. Using variables to pass the input data to the message function
    greeting = input("What is your greeting? ")
    name = input("What is the name of the greeted? ")
    pe2.message(greeting=greeting, name=name)
    
    # 2. Using the input function as a parameter inside the call to the message 
    # function directly.
    pe2.message(greeting=input("What is your quest? "), 
                name=input("what is your favorite color? "))

if __name__ == "__main__":
    main()

# Message function checklist:
# x Reuse the message function in another script
# x Get input from the user
# - Change the greeting based on the time of day
# - Print to a file    
