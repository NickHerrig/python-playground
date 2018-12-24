#! python3
# phoneEmailExtractor.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# This block creates a regex for phone numbers 
phoneRegex = re.compile(r'''(
     (\d{3}|\(\d{3}\))?                         # area code
     (\s|-|\.)?                                 # separator
     (\d{3})                                    # first 3 digits
     (\s|-|\.)                                  # separator
     (\d{4})                                    # last 4 digits
     (\s*(ext|x|ext.)\s*(\d{2,5}))?             # extension
     )''', re.VERBOSE)



# This block creates a regex for email addresses
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # domain name 
        (\.[a-zA-Z]{2,4})   # dot-something
        )''',re.VERBOSE)


# TODO: Find regex matches for email/phone in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):


for groups in moEmail = emailRegex.findall(text):


# TODO: Copy results to the clipboard
