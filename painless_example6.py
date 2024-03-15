# Painless Python
# A ridiculously deep dive into the the print function

# example 5
# Printing messages to a file to build a table template and filling it out with a loop
fileName = "presidents.md"
title = "American Presidents"

column = ["Number", "Name", "Birth Date"]

row1 = ["1", "George Washington", "XXXX"]
row2 = ["2", "John Adams", "XXXX"]
row3 = ["3", "Thomas Jefferson", "XXXX"]

print(f"# {title}\n", file=open(fileName, "a"))
print(f"| {column[0]}", f"{column[1]}", f"{column[2]} |", sep=" | ", file=open(fileName, "a"))
print("| --- | --- | --- |", file=open(fileName, "a"))

for row in [row1, row2, row3]:
    print(f"| {row[0]}", f"{row[1]}", f"{row[2]} |", sep=" | ", file=open(fileName, "a"))