# Painless Python
# A ridiculously deep dive into Python by way of the the print function

# Let's pretend we have a problem to solve!

# Let's say that every month we have to grab data from a spreadsheet and create a table that presents that data in a chart

# This table is called the monthly presidential birthday briefing We also have include a fun fact about each president
 
# How can our limited knowledge of Python help us automate this this exciting and mission critical task?

# Here's our todo list:
# - Figure out how to create a markdown file that contains a chart
# - Figure out how to grab data for particular month from a spreadsheet
# - Figure out how to merge the data in in the spreadsheet with the chart
# - Figure out how to automate the process of creating the chart in markdown

# Example 4.1
# Figure out how to create a markdown file that displays a chart

def main():
    generate_chart()

def generate_chart():
    file_name = "painless_example4_1.md" # The name of the markdown file
    title = "American Presidents Birthday Briefing" # The title of the chart

    column = ["Name", "Birth Date", "Fun Fact"] # The titles of the columns

    # Sample data for the chart (in the form of three lists)
    row1 = ["George Washington", 
            "Feb 22, 1732", 
            "Height: 6'2\", 1/2 inch shorter than Jefferson"] # List 1
    row2 = ["John Adams", 
            "Oct 30, 1735", 
            "Weight: 165 lbs, 10 lbs less than than Washington"] # List 2
    row3 = ["Thomas Jefferson", 
            "Apr 13, 1743", 
            "Died on the same day as John Adams, July 4, 1826"] # List 3

    # Write the chart title to the markdown file
    print(f"# {title}\n", 
          file=open(file_name, "a"))

    # Write the column titles to the markdown file
    print(f"| {column[0]} | {column[1]} | {column[2]} |", 
          file=open(file_name, "a"))

    # Write column formatting to the markdown file
    print("| --- | --- | --- |", 
          file=open(file_name, "a"))

    # For each row write that row's data to the markdown file
    for row in [row1, row2, row3]: 
        # This a for loop, it repeats for each element in a list
        print(f"| {row[0]} | {row[1]} | {row[2]} |", 
              file=open(file_name, "a"))
    
# Note: [row1, row2, row2] is list and each of its elements are lists

# This is the format of a markdown table:

# | Col Head | Col Head | Col Head |
# | -------- | -------- | -------- |
# | R1C1     | R1C2     | R1C3     |
# | R2C1     | R2C2     | R2C3     |
# | R3C1     | R3C2     | R3C3     |

# It looks like a table in ASCII characters!

if __name__ == "__main__":
    main()

# Monthly presidential birthday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# - Figure out how to grab data for particular month from a spreadsheet
# - Figure out how to merge the data in in the spreadsheet with the chart
# - Figure out how to automate the process of creating the chart in markdown
