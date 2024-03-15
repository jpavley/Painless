# Painless Python
# A ridiculously deep dive into the the print function

# example 4
# Printing messages to a file using the Markdown format to build a table
print("# Pets and Food\n", file=open("output.md", "a"))
print("| Feline", "Canine", "Rodent |", sep=" | ", file=open("output.md", "a"))
print("| --- | --- | --- |", file=open("output.md", "a"))
print("| Cat", "Dog", "Mouse |", sep=" | ", file=open("output.md", "a"))
print("| Meowmix", "Alpo", "Cheese |\n", sep=" | ", file=open("output.md", "a"))