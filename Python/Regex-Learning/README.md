## Day 1 - Basic Patterns
- `re.search()` finds a match anywhere in the string
- `re.match()` only checks from the beginning — this tripped me up initially
- `re.findall()` returns a list of ALL matches, not just one
- `[bh]at` is a character set — matches "bat" or "hat" but not "cat"
- Source: Python docs, Claude


## Day 2 - Metacharacters
Regex metacharacters are special symbols with unique, non-literal meanings used to define search patterns in text.

Some Important metacharacters:
- '.' (dot): Matches any single character except a newline. Example: c.t matches "cat", "cot", "cut".
- '+' : Matches one or more occurrences of the preceding character/pattern. Example: lo+l matches "lol", "lool", "loool", but not "ll".
- '*' : Matches zero or more occurrences of the preceding character/pattern. Example: lo*l matches "ll", "lol", "lool".
