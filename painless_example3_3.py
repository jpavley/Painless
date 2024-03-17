# Painless Python
# A ridiculously deep dive into the the print function
import datetime as dt # Import the datetime module so we can tell time
import painless_example2_4 as pe2

# Example 3.2
# Change the greeting based on the time of day

def main():
    # This is a conditional statement: if something is true do this, else do that
    if dt.datetime.now().hour < 12:
        greeting = "Good morning"
    else:
        greeting = "Good afternoon"
    pe2.message(greeting=greeting, name="Aida")

# This logic is a little hard to test...
# We have to wait until the morning or afternoon to see if it works
# How could we fix that?

if __name__ == "__main__":
    main()
    
# Message function checklist:
# x Reuse the message function in another script
# x Get input from the user
# x Change the greeting based on the time of day
# - Print to a file
# - Can we find a better way to "print" to the terminal and to files