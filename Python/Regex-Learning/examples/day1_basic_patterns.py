# day1_basic_patterns.py
# Topic: Regex Basics - literal matching & core functions

import re

# 1. Literal string matching

text = "The quick brown fox jumps over the lazy dog"

# re.search() -> finds first match anywhere in the string
result = re.search("fox", text)
print("search():", result) # <re.Match object; span=(16, 19), match='fox'>

#re.match() -> only check the begining of the text
result2 = re.match("The", text)
print("match():", result2) # <re.Match object; span=(0, 3), match='The'>

result3 = re.match("fox", text) # it will not match because re.match() only check first string
print("match(): ", result3) # None

# 2. Using .group() to extract the matched text
if result:
    print("Matched word:", result.group())

# 3. findall() -> returns ALL matches as a list
text2 = "cat bat hat mat"
result4 = re.findall("at", text2)
print("findall():", result4)  # ['at', 'at', 'at', 'at']

# 4. Basic character sets [ ]
text3 = "cat bat hat mat"
result4 = re.findall("[bh]at", text3)  # matches "bat" or "hat"
print("character set:", result4)  # ['bat', 'hat']

# 5. Case sensitivity (and how to ignore it)
text3 = "Python is FUN"
print(re.findall("fun", text3))                      # [] - case sensitive
print(re.findall("fun", text3, re.IGNORECASE))       # ['FUN']


# Problem I faced today

# 1. Confused re.match() with re.search() at first
#   - re.match() only checks start from the string
#   - re.search() it search in the whole text
#   Fix: tested both on the same string to see the difference
