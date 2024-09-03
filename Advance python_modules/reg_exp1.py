
# pattern structure of a string we looking for 

# regex allows us to search for general patterns in text data

# for example emails - text + @ text + .com is what we will be looking for 

# the re library allows us to create specialized pattern strings and search for mathces in text

# dont memorize these patterns 
# look up the patterns online 

# phone -> (555)-555-5555
# regex -> r"(\d\d\d)-\d\d\d-\d\d\d\d"   or
# regex -> r"(\d{3})-\d{3}-\d{4}"
#  \d stands for digit


text = "the agents phone number is 408-555-1234 call soon  "

'phone ' in text 

import re 

pattern = 'phone'
print(re.search(pattern,text)) # reports back indexes where it is located

pattern = 'not'

print(re.search(pattern,text)) # none 


pattern = 'phone'
match =re.search(pattern,text)

match.span()

match.start()
match.end()

text = 'my phone once, my phone twice'

match = re.search('phone',text)

matches = re.findall('phone',text)
print(matches)
print(len(matches))

for match in re.finditer('phone',text):
    print(match.span())
    print(match.group())






