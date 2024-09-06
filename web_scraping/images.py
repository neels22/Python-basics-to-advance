
import requests
import bs4

# extracting images from a website and storing it in out computer 

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = bs4.BeautifulSoup(res.text,'lxml')
computer = soup.select('.mw-file-element')[0]
print(computer['src'])

# after the img tag take the src and put https before the link and then using below code you can store the image
image_link = requests.get('https://upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png')
print(image_link.content) # gives binary file 

f = open('imagefrominternet.png','wb') # binary file 

f.write(image_link.content)
f.close()