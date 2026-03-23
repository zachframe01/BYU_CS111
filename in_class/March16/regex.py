# experiment with a regex interpreter at: https://regex101.com/

import re

# re.match, re.search, and re.fullmatch take a regular expression (as a raw string) and
# a string of text to match. They return either a Match object or, if there is no match, None

# re.fullmatch requires that the pattern matches the entirety of the string:
print(re.fullmatch(r'-?\d+', '123'))
print(re.fullmatch(r'-?\d+', '123 peeps'))

# Match objects are treated as true values, so you can use the result as a boolean:
print(bool(re.fullmatch(r'-?\d+', '123')))
print(bool(re.fullmatch(r'-?\d+', '123 peeps')))

# re.search returns a match object representing the first occurrence of pattern within string.
title = "I Know Why the Caged Bird Sings"
print(bool(re.search(r'Bird', title)))

# Match objects also carry information about what has been matched. 
# The .group() method allows you to retrieve it. 
x = "This string contains 35 characters."
mat = re.search(r'\d+', x)
print(mat.group(0))

# If there are parentheses in a patterns, each of the parenthesized groups will become 
# groups in the match object.
x = "There were 12 pence in a shilling and 20 shillings in a pound."
mat = re.search(r'(\d+)[a-z\s]+(\d+)', x)
print(mat.group(0))
print(mat.group(1))
print(mat.group(2))
print(mat.groups())

# re.findall() returns a list of strings representing all matches of pattern within string, 
# from left to right.
locations = "AL 36362, MD 21221, UT 84660"
print(re.findall(r'\d\d\d\d\d', locations))

# we can use the compile() function to create a regular expression object that can be reused
regex = re.compile(r'\d{5}')
locations = "AL 36362, MD 21221, UT 84660"
print(regex.findall(locations))
print(re.findall(regex,locations))
locations2 = "UT 84602, MD 20740, CA 94043"
print(regex.findall(locations2))

# Exercise: 
# Create a regular expression that matches:
# a street number of between 1 and 5 digits inclusive, followed by
# a street name - one or more words, each of any length, followed by
# a street type - must be exactly "Dr" or "St" or "Av" or "Ln", followed immediately by a comma, then
# a city name - one word of any length, followed by another comma, then
# a state abbreviation -  exactly 2 uppercase letters from A-Z, followed by 
# a zip code - exactly 5 digits
# a single blank should separate each of the above items, unless a comma has also been specified

# Insert your regular expression into the code below to compile it and find and print all the matches in this string:
# "1296 Eastview Ln, Alpine, UT 84004; 356 University Ave, Provo, UT 84601; 10818 Tanglewood Dr, Heber, UT 84032"
# Hint: to find the complete matching addresses, you may need to put parentheses around the entire pattern in the regex string
# and when matching the street type you may need to use parentheses that don't capture a group - (?: ....)

pattern =re.compile(r'')
matches = re.findall(pattern,"1296 Eastview Ln, Alpine, UT 84004; 356 University Av, Provo, UT 84601; 10818 Tanglewood Dr, Heber, UT 84032")
print(matches) 

# ambiguous matches
# When there are parenthesized groups, Python resolves ambiguity in favor of the first option.
mat = re.match(r'wind|window', 'window')
print(mat.group())

mat = re.match(r'window|wind', 'window')
print(mat.group())

mat = re.match(r'(wind|window)(.*)shade', 'window shade')
print(mat.groups())

mat = re.match(r'(window|wind)(.*)shade', 'window shade')
print(mat.groups())

# ambiguous quantifiers
# Python matches *greedily*, matching the pattern left-to-right and, when given a choice, 
# matching as much as possible while still allowing the rest of the pattern to match
mat = re.match(r'(x*)(.*)', 'xxx')
print(mat.groups())

mat = re.match(r'(x+)(.*)', 'xxx')
print(mat.groups())

mat = re.match(r'(x?)(.*)', 'xxx')
print(mat.groups())

mat = re.match(r'(.*)/(.+)', '12/10/2020')
print(mat.groups())

# Lazy operators
# The operators *?, +?, and ?? match only as much as necessary for the whole pattern to match.
mat = re.match(r'(.*)(\d*)', 'I have 5 dollars')
print(mat.groups())

mat = re.match(r'(.*?)(\d+)', 'I have 5 dollars')
print(mat.groups())

mat = re.match(r'(.*?)(\d*)', 'I have 5 dollars')
print(mat.groups())

