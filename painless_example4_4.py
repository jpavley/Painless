# Example 4.3
# Figure out how to automate the process of creating the chart in markdown

# Note that we had to learn how to code, learn the why Python works and its
# syntax and libaries

# That was a lot of work and there is more work to do
# We only scratched the surface of what we can do with Python

# And we didn't fully achive our goal of automating the process
# The "fun fact" is "hard problemn" for a script

# Let's try to get ChatGPT to do the work for us!

# I installed the OpenAI Python package with pip
from openai import OpenAI
# I'm storying my OpenAI API key in a .env file so you can't steal it!
from dotenv import load_dotenv
# I'm using the os library to load the environment variables
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# Get the OpenAI client
client = OpenAI()

# Get a response from OpenAI
completion = client.chat.completions.create(
  # The model we want to use (to save money we could use gpt-3.5-turbo 
  # but the response might not be as good as gpt-4)
  model="gpt-4",
  # Send to prompt to the model
  # The whole trick here is figure out a prompt that will get the model to do what we want
  # Sometimes its not easy, but its not codoing, its natural language
  messages=[
    # The system role explains to the model what kind of helper we want it to simulate
    {"role": "system", "content": "You are a research assistant, expert in the presidents of the united states and you have a dry sense of humor."},
    # The user roles asks the model what the task is
    {"role": "user", "content": "Create a table with the following information. The title of the table is 'American Presidents Birthday Briefing'. The subtitle is 'Updated as of {current month} {current year}'. Inside the braces are variables that you should replace with the current month the current year. For example 'Updated as of March 2024'. The column headers of the table should be 'Name', 'Birthday', and 'Fun Fact'. For each president born in the current month table will have a row corresponding to that presidents name, birthday, and a fun fact. The fun fact is an short and amusing anecdote about that president. The whole table should be written to a file in markdown format. Just provide the markdown, no comments."}
  ]
)

# The name of the markdown file
file_name = "painless_example4_4.md"
# Write the OpenAI response to a file
print(completion.choices[0].message.content, file=open(file_name, "w"))

#print(completion.choices[0].message.content, file=open(file_name, "w"))

# Monthly presidential brithday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# x Figure out how to grab data for particular month from a spreadsheet
# x Figure out how to merge the data in in the spreadsheet with the chart
# x Figure out how to automate the process of creating the chart in markdown


