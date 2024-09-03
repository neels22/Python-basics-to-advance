

# \d    digits 
# \w    alphanumeric (includes underscore)
# \s    white spaces
# \D    non digits
# \W    non-aplhanumeirc 
# \S    non whitespaces

import re

text = 'my phone number is 405-342-2323'

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)
print('\n')
print(phone.group())  #returns the actual piece of string that mathces 
print('\n')

# better way to do 

# Quantifies 
#  +       occurs one or more times
#  {3}     occurs 3 times
#  {2,4}   occurs 2 to 4 times
#  {3,}    occurs 3 or more times
#  *       occurs zero or more times
#  ?      once or more

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone.group())


# grouping them -- so we can grab only a part of pattern when we want just put pattern in ()
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
print(results.group(3))