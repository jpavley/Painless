# Painless Python
# A ridiculously deep dive into the the print function

def main():
    hello1()
    hello2()
    hello3()
    hello4()

# Example 2.1
# Printing a message to the terminal using a variable
def hello1():
    name = "John"
    print("Hello, " + name + "!")

# Example 2.2
# Printing a message to the terminal using a variable and the f-string
def hello2():
    name = "Paul"
    print(f"Hello, {name}!")

# Example 2.3
# Printing a message to the terminal using a variable and the format method
def hello3():
    name = "George"
    print("Hello, {}!".format(name))

# Example 2.4
# Printing a message to the terminal using two variables and the format method
def hello4():
    greeting = "Goodbye"
    name = "Ringo"
    print("{}, {}!".format(greeting, name))
    
if __name__ == "__main__":
    main()
