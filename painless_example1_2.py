# Painless Python
# A ridiculously deep dive into Python by way of the print function

# Example 1.2
# Importing a script

# Import example 1.1 as a module and give it the alias "pe1"
import painless_example1_1 as pe1

def main():
    pass

if __name__ == "__main__":
    print(__name__)
    main()
else:
    print(__name__)
    pass

# What did we see in the terminal when this script was executed?