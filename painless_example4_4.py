# Example 4.3
# Figure out how to automate the process of creating the chart in markdown

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a research assistant, expert in the presidents of the united states and you have a dry sense of humor."},
    {"role": "user", "content": "Create a table with the following information. The title of the table is 'American Presidents Birthday Briefing'. The subtitle is 'Updated as of {current month} {current year}'. Inside the braces are variables that you should replace with the current month the current year. For example 'Updated as of March 2024'. The column headers of the table should be 'Name', 'Birthday', and 'Fun Fact'. For each president born in the current month table will have a row corresponding to that presidents name, birthday, and a fun fact. The fun fact is an short and amusing anecdote about that president. The whole table should be written to a file in markdown format."}
  ]
)

file_name = "painless_example4_4.md"
print(completion.choices[0].message, file=open(file_name, "a"))

# Monthly presidential brithday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# x Figure out how to grab data for particular month from a spreadsheet
# x Figure out how to merge the data in in the spreadsheet with the chart
# x Figure out how to automate the process of creating the chart in markdown


