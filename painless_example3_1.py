# Painless Python
# A ridiculously deep dive into the the print function

# Example 3.1
# Reuse the message function in another script

# loead the painless_example2_4.py script as a module
# (not running it, just loading it)
import painless_example2_4 as pe2

def main():
    pe2.message(greeting="Hail elf friend", name="Frodo")
    pe2.message(greeting="You shall not pass", name="Balrog")

    
if __name__ == "__main__":
    main()