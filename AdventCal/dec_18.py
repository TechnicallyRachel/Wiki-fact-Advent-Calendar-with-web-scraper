#webscraped historic fact from https://en.wikipedia.org/wiki/December_18

from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/December_18'
 
page = urlopen(url)

soup = BeautifulSoup(page,'lxml')

# gets all text (with html) from wanted paragraph entry
x = soup.find(text='1892').parent.parent

#gets rid of the html and prints only the text with get_text() command
print x.get_text()
