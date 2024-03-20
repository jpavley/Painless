# Painless Python
# A ridiculously deep dive into the the print function
import datetime as dt # Import the datetime module so we can tell time
# import painless_example2_4 as pe2 # This line is commented out, Why?

# Example 3.4
# Print to a file

def message(greeting, name, file_name):
    if file_name:
         # There is a file_name
        file = open(file_name, "a") # Create and open file in append mode
        print(f"{greeting}, {name}!", file=file) # Send data to file
    else:
        # There is no file_name
        print(f"{greeting}, {name}!") # Send data to terminal

def main():    
    # Just for testing we'll send the message to the terminal and then a file
    message(greeting="Sup", name="Beth", file_name=None)
    message(greeting="Hi", name="Beth", file_name="painless_example3_4.txt")

# What is a file?
# What happens if fileName is " "?
# Does the open function do?
# What does the "a" mean?
# What other file modes are there for writing data?

if __name__ == "__main__":
    main()
    
# Message function checklist:
# x Reuse the message function in another script
# x Get input from the user
# x Change the greeting based on the time of day
# x Print to a file

# Now it feels like have some real tools in our tookit!
# Let's do something serious with our message function!