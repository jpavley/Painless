# Painless Python
# A ridiculously deep dive into the the print function

# example 5
# Printing messages to a file to build a table template and filling it out with variables and arrays
fileName = "presidents.md"
title = "American Presidents"

column = ["Number", "Name", "Birth Date"]

row1 = ["1", "George Washington", "XXXX"]
row2 = ["2", "John Adams", "XXXX"]
row3 = ["3", "Thomas Jefferson", "XXXX"]

print(f"# {title}\n", file=open(fileName, "a"))
print(f"| {column[0]}", f"{column[1]}", f"{column[2]} |", sep=" | ", file=open(fileName, "a"))
print("| --- | --- | --- |", file=open(fileName, "a"))
print(f"| {row1[0]}", f"{row1[1]}", f"{row1[2]} |", sep=" | ", file=open(fileName, "a"))
print(f"| {row2[0]}", f"{row2[1]}", f"{row2[2]} |", sep=" | ", file=open(fileName, "a"))
print(f"| {row3[0]}", f"{row3[1]}", f"{row3[2]} |", sep=" | ", file=open(fileName, "a"))