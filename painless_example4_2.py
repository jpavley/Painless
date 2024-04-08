# Painless Python
# A ridiculously deep dive into the the print function

# Example 4.2
# Figure out how to grab data for particular month from a spreadsheet

# I found a great CSV file that contains the birth dates and other interesting facts about presidents

# Let's see if we can open it up and grab data based on the current month

# This task is a complicated job. Lets get help from the Python community:
import pandas as pd # Pandas is a module that let us work with CVS data
import re # RE is a module that let us use regular expressions to filter data
import datetime # We used this before to deal with dates and times

def main():
    get_presidents()

def get_presidents():
    # Get the current month
    currentMonth = datetime.datetime.now().month
    
    # Get the name of our data file
    fileName = "US-Presidents.csv"
    
    # Use Pandas to read this data file into a data frame 
    # (it's like spread sheet)
    df = pd.read_csv(fileName)
        
    # 1. There are extra characters appended to some of the dates; These characters prevent the date strings from being parsed into a date object by DateTime.
    df['Born'] = df['Born'].apply(clean_date)
    
    # (.apply() is a way to call a function on every element of a list)
    
    # 2. The date strings are in two different formats and some of the date are missing the century digits We use this .apply to convert all the date strings in the Born column into TimeStamp objects
    df['Born'] = df['Born'].apply(parse_dates) 
    
    # 3. Now we can get the row data (in a new data frame) for just the current month
    data = get_data_in_range(df, currentMonth, currentMonth)
    
    # The new data frame has four columns: President, Born, Height (ft), and Weight (lbs)
    # We access them by their column index (0 through 3)
    
    president_names = data[:,0]     # Create a list of names
    president_birthdays = data[:,1] # Create a list of birthdays
    president_heights = data[:,2]   # Create a list of heights
    president_weights = data[:,3]   # Create a list of weights
    
    # We broken them in to 4 lists because I thought that would be easiest to to merge into an f-string with 4 different variables. The index of each element in each list is a key that keeps the lists in sync

    for i in range(len(president_names)):
        # for each president found print a string
        print(f"{president_names[i]} was born on {president_birthdays[i].strftime('%B %d, %Y')}. He weighed {president_weights[i]} lbs and was {president_heights[i]} ft. tall.")

def clean_date(date_string):
    # Data problem #1: "Feb 22, 1732[a]"
    # The "[a]" prevents Pandas from recognizing the string as a date
    
    # Remove characters in square brackets using regular expressions
    cleaned_date = re.sub(r"\[.*\]", "", date_string)
    
    # r"\[.*\]" is a regular expression that matches any pattern of characters that look like "[a] (brackets with any single character inside them)
    
    # The re.sub() replaces the matched characters with an empty string--which is a way to delete them
    return cleaned_date

def parse_dates(date):
    # Data problem #2: Some date strings looks like "Feb 22, 1732" and some 
    # date strings look like "20-Nov-42"
    # We need to tell Pandas to parse both patterns
    
    # We have two date patterns in our data: '%b %d, %Y' and '%d-%b-%y'
    for fmt in ("%b %d, %Y", "%d-%b-%y"): # loop with each pattern
        try:
            # Try to convert the date string into a TimeStamp object using the 
            # current pattern (This could fail and if so the function will jump 
            # to the except clause below)
            date_obj = pd.to_datetime(date, format=fmt)
            
            # If the date string was successfully converted in a TimeStamp
            # we get here
            
            # Data problem #3: Date strings like "20-Nov-42" convert into
            # November 20, 2042 and all presidents (so far) were born
            # in the 1900s!
            
            # If the year of the parsed date is greater than 2000 and the 
            # format used was "%d-%b-%y", it means the year is in the 1900s, 
            # not the 2000s
            
            # So, we have to subtract 100 from the year to get to the previous
            # century
                        
            if date_obj.year > 2000 and fmt == "%d-%b-%y":
                # Replace the current year part of the TimeStamp with
                # the same year from the previous century
                date_obj = date_obj.replace(year=date_obj.year - 100)
            
            # Great Success! return the datetime object to the caller
            return date_obj
        
        except ValueError:
            # If a the function could not convert the date string into a
            # TimeStamp object, it means the format of the string does not 
            # match the expected pattern. So, we pass, go back to the top
            # of the function and try the next pattern.
            pass
    
    # If none of the patterns match we end up here
    # In this case the function will return NaT (Not a Time), which is 
    # the equivalent of NaN (Not a Number) for datetime objects
    return pd.NaT

def get_data_in_range(df, start_month, end_month):
    # Drop duplicate rows
    # Why do we have duplicate rows? Because some presidents have more than
    # one term or are appear in more than one row in the data set
    df = df.drop_duplicates(subset="President")
    
    # subset="President" means use the values in the President column as the 
    # key upon which to identify duplicates
        
    # Filter the DataFrame to include only rows where the month of the 
    # Born column is within the specified range
    
    # Create a filter that only includes the the data of the presidents who 
    # were born within the specified range
    mask = df["Born"].dt.month.between(start_month, end_month)
    
    # A mask applied to a data frame will ignore any data that doesn't match
    # the filter (its like a database query)
    
    # Create a new data frame that only contains the columns that are 
    # interesting to us
    data = df.loc[mask, ["President", "Born", "Height (ft)", "Weight (lbs)"]]
    
    # Return just the value in the new data frame
    return data.values

if __name__ == "__main__":
    main()

# Monthly presidential birthday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# x Figure out how to grab data for particular month from a spreadsheet
# - Figure out how to merge the data in in the spreadsheet with the chart
# - Figure out how to automate the process of creating the chart in markdown
