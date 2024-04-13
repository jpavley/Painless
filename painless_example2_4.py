# Painless Python
# A ridiculously deep dive into Python by way of the print function

# Example 2.3 is much less hard coded than before
# It still contains some hard coding:
# - We have to write repetitive code 

# Example 2.4
# Printing a message to the terminal using a list and a for loop

def main():
    # for loop repeats itself for each element in a list
    for name in ["John", "Paul", "🤨", "こんにちは"]: 
        # the "name" variable's value is to the next element in the list each time the loop repeats
        message(name)

# What does the command "for" tell Python to do?
# What does the command "in" tell Python to do?
    
def message(name: str):
    print(f"Hello, {name}!") # two arguments merged into one string
    
# What else can we do with the with our message function?
# - Reuse the message function in another script
# - Get input from the user
# - Change the greeting based on the time of day
# - Print to a file
    
if __name__ == "__main__":
    main()
