# Painless Python
# A ridiculously deep dive into Python by way of the the print function
import painless_example2_4 as pe2

# Example 3.2
# Get input from the user

def main():
    # Two ways to call the message function with user input:
    
    # 1. Using variables to pass the input data to the message function
    name = input("What is your name? ")
    pe2.message(name)
    
    # 2. Using the input function as a parameter inside the call to the message function directly.
    pe2.message(input("What is your pet's name? "))
    
if __name__ == "__main__":
    main()

# Message function checklist:
# x Reuse the message function in another script
# x Get input from the user
# - Change the greeting based on the time of day
# - Print to a file    
