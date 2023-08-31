import requests
from bs4 import BeautifulSoup
# Set the URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Web_scraping'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
heading = soup.find('h1').text
paragraph = soup.find('p').text
print(heading)
print(paragraph)

