# Painless Python
# A ridiculously deep dive into the the print function

# Example 2.1
# Printing a message to the terminal using a variable
name = "John"
print("Hello, " + name + "!")

# Example 2.2
# Printing a message to the terminal using a variable and the f-string
name = "Paul"
print(f"Hello, {name}!")

# Example 2.3
# Printing a message to the terminal using a variable and the format method 
name = "George"
print("Hello, {}!".format(name))

# Example 2.4
# Printing a message to the terminal using two variables and the format method
greeting = "Goodbye"
name = "Ringo"
print("{}, {}!".format(greeting, name))