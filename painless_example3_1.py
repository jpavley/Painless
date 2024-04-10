# Painless Python
# A ridiculously deep dive into Python by way of the print function

# Example 3.1
# Reusing a function from another script

import painless_example2_4 as pe2 # Load the message script with an easy to type name

def main():
    pe2.message(name="Frodo")


# We reached inside the pe2 script (aka painless_example2_4.py) to call the message script
# Once loaded the pe2 script has become a module which can be used by any other script

if __name__ == "__main__":
    main()
    
# Message function checklist:
# x Reuse the message function in another script
# - Get input from the user
# - Change the greeting based on the time of day
# - Print to a file