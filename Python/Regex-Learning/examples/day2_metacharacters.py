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



