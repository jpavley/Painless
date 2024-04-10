# Painless Python
# A ridiculously deep dive into Python by way of the print function

# Example 4.4
# Figure out how to automate the process of creating the chart in markdown

# Note that we had to learn how to code, learn the why Python works and its
# syntax and libraries

# That was a lot of work and there is more work to do
# We only scratched the surface of what we can do with Python

# And we didn't fully achieve our goal of automating the process
# The "fun fact" is "hard problem" for a script

# Let's try to get ChatGPT to do the work for us!

# I installed the OpenAI Python package with pip
from openai import OpenAI # pip3 install openai
# I'm storying my OpenAI API key in a .env file so you can't steal it!
from dotenv import load_dotenv # pip3 install python-dotenv
# I'm using the os library to load the environment variables
import os
# Let's reuse the file name generator from the previous example
import painless_example4_3 as pe4_3
import datetime

def main():
  # Load environment variables from .env file
  load_dotenv()

  # Retrieve the API key from environment variables
  OpenAI.api_key = os.getenv('OPENAI_API_KEY')

  # Get the OpenAI client
  client = OpenAI()

  current_month_index = datetime.datetime.now().month
  current_month_name = pe4_3.get_month_from_int(
      current_month_index).strftime("%B")
  current_year = pe4_3.get_month_from_int(current_month_index).year

  # Get a response from OpenAI
  completion = client.chat.completions.create(
    # The model we want to use
    model="gpt-4",
    # Send prompt to the model
    # The whole trick here is figure out a prompt that will get the model to do what we want it to do
    # Sometimes its not easy, but its not coding, its natural language
    messages=[
      # The system role explains to the model what kind of helper we want it to simulate
      {"role": "system", "content": "You are a research assistant, expert in the presidents of the united states and you have a dry sense of humor."},
      # The user roles explains the task to the model
      {"role": "user", "content": f"Create a table with the following information: The title of the table is 'American Presidents Birthday Briefing'. The subtitle is 'Updated as of {current_month_name} {current_year}'. The column headers for the table should be 'Name', 'Birthday', and 'Fun Fact'. For each president born in the {current_month_name} month the table will have a row corresponding to that presidents name, birthday, and a fun fact. The fun fact is a short and amusing anecdote about the president. Important Note: Include all the presidents born in {current_month_name}. Do not include any presidents born in any other months. The whole table should be written as a file in markdown format. Just provide the markdown, no introduction, no comments, no notes, no code fencing, nothing outside the markdown."}
    ]
  )

  # The name of the markdown file
  file_name = pe4_3.generate_unique_file_name(current_month_index, version=1)
  # Write the OpenAI response to a file
  print(completion.choices[0].message.content, file=open(file_name, "w"))

  # The response from OpenAI contains some unwanted characters so let's clean it up
  remove_markdown_code_fencing(file_name)

  # Let the user know the file was created
  print(f"File created: {file_name}")

# This function removes the markdown code fencing from the OpenAI response
# Code fencing: ```markdown and ```` that surrounds the markdown code
def remove_markdown_code_fencing(file_name):
    # Open the file in read mode into a variable
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Loop through each line
        for line in lines:
            # Write each line back to the file but skip the markdown code fencing
            if line.strip("\n") != "```markdown" and line.strip("\n") != "```":
                file.write(line)

if __name__ == "__main__":
    main()

# Monthly presidential birthday briefing todo list:
# x Figure out how to create a markdown file that contains a chart
# x Figure out how to grab data for particular month from a spreadsheet
# x Figure out how to merge the data in in the spreadsheet with the chart
# x Figure out how to automate the process of creating the chart in markdown

# We could have started with OpenAI and skipped most of the coding
# But as impressive as OpenAI is, it's results are inconsistent
# There is much more work to do to figure out how integrate the promise if AI into our work and lives




