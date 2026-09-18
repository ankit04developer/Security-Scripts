#. (Dot)
#Inside the regular expression, a dot represents any character except
#the newline character, which is \n

import re
data = "hello\nworld"
pattern = r''
matches = re.finditer(pattern, data)
for match in matches:
    print(match)
    
    

# Metacharacter '+'
#means preceding expression or character should repeat one or more times
#with as many repetitions as possible.

import re
text = "My email addresses are shantanu@codeyug.com and shantanu10@gmail.com"
pattern =  r'\w+@\w+\.\w+'
email_adderesses = re.findall(pattern, text)
print(email_adderesses)



# Metacharacter '*'
# a* matches zero or more 'a' characters, including zero occurrences.

import re
data = "hello Ankit"
pattern = r'l*'
matches = re.findall(pattern, data)
print(matches)



# Metacharacter '^'
# It ensure that the pattern only matches when it appears at the beginning of the text.

import re
data = "4hello Ankit"
pattern = r'^\d'
matches = re.findall(pattern, data)
if matches:
    print("Starting with digits.")
else:
    print("Not starting with digits.")

# negation of character classes

# In this example: [^0-9] matches any single character that is not a digit.
import re
data = "hello 10 11world"
pattern = r"[^0-9]"
matches = re.findall(pattern, data)
print(matches)


# Metacharacter '$'
# used to match the end of a line or the end of data.
# It is just opposite of '^'

import re
data = '''hello Ankit333
i am anish123'''
pattern = r'\d{3}$'
matches = re.finditer(pattern, data, re.MULTILINE)
for match in matches:
    print(match)

