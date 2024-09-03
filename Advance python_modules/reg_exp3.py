
#wildcard characters 
#  pipe operator | --> means or

import re 
print(re.search(r'cat|dog','the cat is here'))


res = re.findall(r'at','the cat is here')
print(res)

# - period .
res = re.findall(r'.at','the cat in the hat sat here')
print(res)

res = re.findall(r'...at','the cat in the hat sat here splat')
print(res)


# ^ string starting with  only the first character
res = re.findall(r'^\d','1 is a number and 2 is a number')
print(res)

# $ string ends with only the last character
res = re.findall(r'\d$' , 'stirng is ending with 4')
print(res)




# excluding anything or removing anything from strings
# common way to get rid of punctuation from  a sentence

phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'

res = re.findall(pattern,phrase)
print(res)

# removing punctuation
text_phrase = 'this is string but it has punctuation. how can we remove it?'
res= re.findall(r'[^!.? ]+',text_phrase)
print(res)
print(' '.join(res))




# including 

text= ' only find the hypen-words in this sentence. but dont know long-ish they are'

pattern = r'[\w]+-[\w]+'

res = re.findall(pattern,text)
print(res)


# multiple options

text = 'heelo would you find a catfish'

res = re.search(r'cat(fish|nap)',text)
print(res)