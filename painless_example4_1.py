# Painless Python
# A ridiculously deep dive into the the print function

# Let's pretend we have a problem to solve!

# Let's say that every month we have to grab data from a spreadsheet 
# and create a table that presents that data in a chart.
# This table is called the monthly presidential brithday briefing.
# We also have include a fun fact about each president.
 
# How can our limited knowlege of Python help us automate this this 
# exciting and mission critical task?

# Here's our todo list:
# - Figure out how to create a markdown file that contains a chart.
# - Figure out how to grab data for particular month from a spreadsheet.
# - Figure out how to merge the data in in the spreadsheet with the chart using Python.
# - Figure out how to automate the process of creating the chart and the markdown file on a monthly basis.

# Example 4.1
# Figure out how to create a markdown file that contains a chart.

def main():
    generate_chart()

def generate_chart():
    file_name = "painless_example4_1.md" # the name of the markdown file
    title = "American Presidents Birthday Briefing" # the title of the chart

    column = ["Name", "Birth Date", "Fun Fact"] # the titles of the columns

    # Sample data for the chart
    row1 = ["George Washington", "Feb 22, 1732", "Height: 6'2\", 1/2 inch shorter than Jefferson"]
    row2 = ["John Adams", "Oct 30, 1735", "Weight: 165 lbs, 10 lbs less than than Washington"]
    row3 = ["Thomas Jefferson", "Apr 13, 1743", "Died on the same day as John Adams, July 4, 1826"]

    # Output the chart title to the markdown file
    print(f"# {title}\n", file=open(file_name, "a"))

    # Output the column titles to the markdown file
    print(f"| {column[0]} | {column[1]} | {column[2]} |", file=open(file_name, "a"))

    # Output column formatting to the markdown file
    print("| --- | --- | --- |", file=open(file_name, "a"))

    # For each row in the sample data, output that row's data to the markdown file
    for row in [row1, row2, row3]:
        print(f"| {row[0]} | {row[1]} | {row[2]} |", file=open(file_name, "a"))

if __name__ == "__main__":
    main()

# Monthly presidential brithday briefing todo list:
# x Figure out how to create a markdown file that contains a chart.
# - Figure out how to grab data for particular month from a spreadsheet.
# - Figure out how to merge the data in in the spreadsheet with the chart using Python.
# - Figure out how to automate the process of creating the chart and the markdown file on a monthly basis.
