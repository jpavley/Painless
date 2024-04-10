# Painless Python
# A ridiculously deep dive into the print function
import datetime as dt # Import the DateTime module so we can tell time

# Example 3.3
# A ridiculously deep dive into Python by way of the the print function

# Refactor the message function to accept two arguments
def message(greeting: str, name: str):
        print(f"{greeting}, {name}!")

def main():
    # This is a conditional statement: if something is true do this, else do that
    if dt.datetime.now().hour < 12:
        # the current hour is less than 12
        greeting = "Good morning"
    else:
        # the current hour is 12 or greater than 12
        greeting = "Good afternoon"
        
    message(greeting, "Alice")

if __name__ == "__main__":
    main()
    
# Message function checklist:
# x Reuse the message function in another script
# x Get input from the user
# x Change the greeting based on the time of day
# - Print to a file