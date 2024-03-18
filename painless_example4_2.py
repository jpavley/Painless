# Painless Python
# A ridiculously deep dive into the the print function

# Example 4.2
# Figure out how to grab data for particular month from a spreadsheet.

# I found a great CSV file that contains the birth dates and other intereasting facts about presidents.
# Let' see if we can open it up and grab data based on the current month.

import pandas as pd
import re # Regular expressions

def main():
    getPresidents()

def getPresidents():
    import datetime
 
    # Get the current month
    currentMonth = datetime.datetime.now().month

    fileName = "US-Presidents.csv"
    df = pd.read_csv(fileName)
    df['Born'] = df['Born'].apply(cleanDate) # Remove characters in square brackets using regular expressions
    df['Born'] = df['Born'].apply(parse_dates) # Convert the date strings into datetime objects

    data = get_data_in_range(df, currentMonth, currentMonth)  # Get data of people born in January, February, or March

    president_names = data[:,0]
    president_birthdays = data[:,1]
    president_heights = data[:,2]
    president_weights = data[:,3]

    for i in range(len(president_names)):
        print(f"{president_names[i]} was born on {president_birthdays[i].strftime('%B %d, %Y')}. He weighed {president_weights[i]} lbs. and was {president_heights[i]} ft. tall.")

def cleanDate(dateString):
    # Remove characters in square brackets using regular expressions
    cleanedDate = re.sub(r"\[.*\]", "", dateString)
    return cleanedDate

def parse_dates(date):
    # We have two date formats in our data: '%b %d, %Y' and '%d-%b-%y'
    for fmt in ('%b %d, %Y', '%d-%b-%y'):
        try:
            # Try to convert the date string into a datetime object using the current format
            date_obj = pd.to_datetime(date, format=fmt)
            
            # If the year of the parsed date is greater than 2000 and the format used was '%d-%b-%y',
            # it means the year is in the 1900s, not the 2000s. So, we subtract 100 from the year.
            if date_obj.year > 2000 and fmt == '%d-%b-%y':
                date_obj = date_obj.replace(year=date_obj.year - 100)
            
            # Return the datetime object
            return date_obj
        except ValueError:
            # If a ValueError is raised, it means the format does not match the date string.
            # So, we pass and try the next format.
            pass
    
    # If none of the formats match, we return pd.NaT (Not a Time), which is the equivalent of NaN for datetime objects.
    return pd.NaT

def get_names_in_range(df, start_month, end_month):
    # Filter the DataFrame to include only rows where the month of the 'Born' column is within the specified range
    mask = df['Born'].dt.month.between(start_month, end_month)
    # Get the names of the people who were born within the specified range
    names = df.loc[mask, 'President'].tolist()
    return names

def get_data_in_range(df, start_month, end_month):
    # Drop duplicate rows
    df = df.drop_duplicates(subset='President')
    # Filter the DataFrame to include only rows where the month of the 'Born' column is within the specified range
    mask = df['Born'].dt.month.between(start_month, end_month)
    # Get the data of the people who were born within the specified range
    data = df.loc[mask, ['President', 'Born', 'Height (ft)', 'Weight (lbs)']]
    return data.values

if __name__ == "__main__":
    main()

# Monthly presidential brithday briefing todo list:
# x Figure out how to create a markdown file that contains a chart.
# x Figure out how to grab data for particular month from a spreadsheet.
# - Figure out how to merge the data in in the spreadsheet with the chart using Python.
# - Figure out how to automate the process of creating the chart and the markdown file on a monthly basis.
