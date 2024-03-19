# Painless Python
# A ridiculously deep dive into the the print function

# Example 3.1
# Reuse the message function in another script

# Load the painless_example2_4.py script as a module
# (not running it, just loading it)

import painless_example2_4 as pe2 # Load the message script with an easy name

def main():
    pe2.message(greeting="Hail elf friend", name="Frodo")
    pe2.message(greeting="You shall not pass", name="Balrog")

# We reached inside the pe2 script (aka painless_example2_4.py) to call the
# message script

# In Python the pe2 script has become a module which can be used by any other
# script

if __name__ == "__main__":
    main()
    
# Message function checklist:
# x Reuse the message function in another script
# - Get input from the user
# - Change the greeting based on the time of day
# - Print to a file