# Painless Python
# A ridiculously deep dive into the the print function
import datetime as dt # Import the datetime module so we can tell time
# import painless_example2_4 as pe2

# Example 3.4
# Print to a file
def message(greeting, name, fileName):
    if fileName:
        file = open(fileName, "a")
        print(f"{greeting}, {name}!", file=file)
    else:
        print(f"{greeting}, {name}!")

def main():
    # This is a conditional statement: if something is true do this, else do that
    if dt.datetime.now().hour < 12:
        greeting = "Good morning"
    else:
        greeting = "Good afternoon"
    message(greeting=greeting, name="Aida", fileName=None)
    message(greeting=greeting, name="Aida", fileName="painless_example3_4.txt")

# What is a file?
# What happens if fileName is ""?
# Does the open function do?
# What does the "a" mean?

if __name__ == "__main__":
    main()
    
# Message function checklist:
# x Reuse the message function in another script
# x Get input from the user
# x Change the greeting based on the time of day
# x Print to a file

# Now it feels like have some real tools in our tookit!
# Let's do something serious with our message function!