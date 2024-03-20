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
import datetime
import pandas as pd

def main():
    generate_presidental_birthday_briefing()

def generate_presidental_birthday_briefing():
    current_month_index = datetime.datetime.now().month
    current_month_name = datetime.datetime.now().strftime("%B")
    current_month_year = datetime.datetime.now().year
    file_name = generate_unique_file_name(current_month_name,
                                          current_month_year)
    data = get_presidential_data_for_current_month(current_month_index)
    generate_chart(file_name,
                   data,
                   current_month_name,
                   current_month_year)
    
    
def generate_unique_file_name(current_month_name, current_month_year):
    # Create a unique file name using the month and year
    file_name = f"pres_briefing_{current_month_name}_{current_month_year}.md"
    return file_name

def get_presidential_data_for_current_month(current_month):
    fileName = "US-Presidents.csv"
    df = pd.read_csv(fileName)
    df['Born'] = df['Born'].apply(pe4_2.clean_date)
    df['Born'] = df['Born'].apply(pe4_2.parse_dates) 
    data = pe4_2.get_data_in_range(df, current_month, current_month)
    return data

def generate_chart(file_name, data, current_month_name, current_month_year):
    title = "American Presidents Birthday Briefing"
    subtitle = "Updated as of"
    column = ["Name", "Birthday", "Height", "Weight"]
    
    print(f"# {title}\n", file=open(file_name, "a"))
    print(f"## {subtitle} {current_month_name} {current_month_year}\n", 
          file=open(file_name, "a"))
    print(f"| {column[0]} | {column[1]} | {column[2]} | {column[3]} |", 
          file=open(file_name, "a"))
    print("| --- | --- | --- | --- |", file=open(file_name, "a"))
    
    for row in data:
        print(f"| {row[0]} | {row[1].strftime('%B %d, %Y')} | {row[2]} | {row[3]} |", 
              file=open(file_name, "a"))

if __name__ == "__main__":
    main()

# Monthly presidential brithday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# x Figure out how to grab data for particular month from a spreadsheet
# x Figure out how to merge the data in in the spreadsheet with the chart
# - Figure out how to automate the process of creating the chart in markdown
