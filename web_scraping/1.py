

import requests # to get the entire page in string form
import bs4 # parsing through the string of html and text 

# grab the title

result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
print(type(result))
# print(result.text)


soup = bs4.BeautifulSoup(result.text,"lxml")

print(soup)

########################
# grab the title , p, h1 etc elements tag

print('\n\n\n')
res = soup.select('h1')[0].get_text()
print(res)

print('\n\n\n')

res = soup.select('p')[1].get_text()
print(res)

print('\n\n\n')

res = soup.select('p')[1].get_text()
print(res)

########################
# grab the class,id 

# print('\n\n\n')
# res = soup.select('#idname')[1].get_text()
# print(res)


# print('\n\n\n')
# res = soup.select('.classname')[1].get_text()
# print(res)


# print('\n\n\n') 
# res = soup.select('div span')[1].get_text() # span inside of div
# print(res)
# print('\n\n\n') 



#####################################################################
result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
print(type(result))
# print(result.text)


soup = bs4.BeautifulSoup(result.text,"lxml")

# print(soup)

items = soup.select(".toctext")

for item in items:
    print(item.text)