#! python3

# Number and Email Search

import re
import pyperclip

content = str(pyperclip.paste())
result = []

phoneregex = re.compile(r"""
(\+\d+|\(\+\d+\))?                       # Area code
(\s|-|\.[,3])?                          # Separator     
(\d+)?                                  # Movil connection
(\s|-|\.[,3])?                          # Separator
(\d+)                                   # Location
(\s|-|\.[,3])?                          # Separator
(\d{4})                                 # First 4 numbers
(\s|-|\.[,3])?                          # Separator
(\d{4})                                 # Last 4 numbers

""", re.VERBOSE)

emailregex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z0-9._%+-]+", re.I)

moemail = emailregex.findall(content)
mophone = phoneregex.findall(content)

for i in mophone:
    var = i[0] + i[2] + i[4] + i[6] + i[8] + " "
    result.append(var)

for i in moemail:
    result.append(i)
    
result = "\n".join(result)

if len(result) > 0:
    pyperclip.copy(result)
    print(f"copied text:\n{result}")

