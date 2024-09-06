
import requests
import bs4

# get the title of book with 2 star rating

base_url= 'https://books.toscrape.com/catalogue/page-{}.html'
page_num= 0
base_url.format(page_num)




res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text,'lxml')

r = soup.select('.product_pod')

example = r[0]
print('star-rating Three' in str(example))


print(example.select('.star-rating Three'))
print(example.select('a')[1]['title'])


two_star_title = []

for n in range(1,51):

    scare_url = base_url.format(n)
    res = requests.get(scare_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        book_title = book.select('a')[1]['title']
        two_star_title.append(book_title)

print(two_star_title)
