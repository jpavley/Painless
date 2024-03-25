# Painless Python
# A ridiculously deep dive into the the print function

# Example 4.3
# Figure out how to merge the data in in the spreadsheet with the chart

# How comes the culmination of our all explorations! 
# We will grab the data from the spreadsheet for the current month
# and use it to create a chart in a markdown file named for the month

# The humble print function is still the heart of our solution
# but we're combining it sophisticated tools from the Python community

# let's resuse the data cleaning and parsing functions
import painless_example4_2 as pe4_2

# Some other imports we'll need
import datetime
import pandas as pd # pip3 install pandas

def main():
    generate_presidental_birthday_briefing()

# This is the function that does all the work
def generate_presidental_birthday_briefing():
    # Get the current month from the system clock
    current_month_index = 12 # datetime.datetime.now().month
    # Get the file name based on the current month index
    file_name = generate_unique_file_name(current_month_index)
    # Get the president data for the current month
    data = get_presidential_data_for_current_month("US-Presidents.csv", 
                                                   current_month_index)
    # Make the chart and write it to a file in markdown format
    generate_chart(file_name, data, current_month_index)
    
# This function creates a unique file name which includes the month and year
def generate_unique_file_name(current_month_index, version=0):
    # Make the month name from the it's index number
    current_month_name = get_month_from_int(current_month_index).strftime("%B")
    # Make the year digits from the month
    current_month_year = get_month_from_int(current_month_index).year
    # Make the the file_name gluing it all together in an f-string
    file_name = f"pres_briefing_{current_month_name}_{current_month_year} v{version}.md"
    return file_name

# This function grabs data from the CSV file for the current month
# and returns it as a list of lists
def get_presidential_data_for_current_month(file_name, current_month_index):
    # make a data frame by reading all the data in form the CSV file
    df = pd.read_csv(file_name)
    # clean the date and parse it into a datetime object
    df['Born'] = df['Born'].apply(pe4_2.clean_date)
    df['Born'] = df['Born'].apply(pe4_2.parse_dates)
    # get just the rows of data for the current month
    data = pe4_2.get_data_in_range(df, current_month_index, current_month_index)
    return data

# This function returns a datetime object for a month given an integer
def get_month_from_int(month_int):
    # Start with the current DateTime as a default
    current_year = datetime.datetime.now().year
    # Return a DateTime for the given month index
    return datetime.datetime(current_year, month_int, 1)

# This function creates a chart in a markdown file with all the data
# from the spreadsheet for the current month
def generate_chart(file_name, data, current_month_index):
    # Make all the parts we need for the title, subtitle, and column names
    title = "American Presidents Birthday Briefing"
    subtitle = "Updated as of"
    column = ["Name", "Birthday", "Height", "Weight"]
    # Make the month name and year from the current month index
    current_month_name = get_month_from_int(current_month_index).strftime("%B")
    current_month_year = get_month_from_int(current_month_index).year
    
    # We're writing to the file a little differently this time
    # First we open the file in write mode
    # Then we print each line of the chart to the file
    with open(file_name, "w") as file:
        print(f"# {title}\n", file=file)
        print(f"## {subtitle} {current_month_name} {current_month_year}\n", 
              file=file)
        print(f"| {column[0]} | {column[1]} | {column[2]} | {column[3]} |", 
              file=file)
        print("| --- | --- | --- | --- |", file=file)
        for row in data:
            print(f"| {row[0]} | {row[1].strftime('%B %d, %Y')} | {row[2]} | {row[3]} |", 
                  file=file)

if __name__ == "__main__":
    main()

# Monthly presidential brithday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# x Figure out how to grab data for particular month from a spreadsheet
# x Figure out how to merge the data in in the spreadsheet with the chart
# - Figure out how to automate the process of creating the chart in markdown
