# Painless Python
# A ridiculously deep dive into the the print function

# Example 2.3 is much less hard coded than before but it still contains some 
# hard coding because it can only say hello

# Example 2.4
# Printing a message to the terminal using two variables inside an f-string

def main():
    message(greeting ="Yo", name="Ringo") # pass a greeting and a name
    
def message(greeting, name):
    print(f"{greeting}, {name}!") # two arguments merged into one string
    
# Note that we wrapped the print function in a function called message
# If we find something better than the print function we need only to change 
# the message function and not all the code than calls the message function
    
# What else can we do with the with our message function?
# - Reuse the message function in another script
# - Get input from the user
# - Change the greeting based on the time of day
# - Print to a file
    
if __name__ == "__main__":
    main()
