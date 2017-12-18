#webscraped historic fact from https://en.wikipedia.org/wiki/December_9

from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/December_9'
 
page = urlopen(url)

soup = BeautifulSoup(page,'lxml')

# gets all text (with html) from wanted paragraph entry
x = soup.find(text='A Charlie Brown Christmas').parent.parent.parent

#gets rid of the html and prints only the text with get_text() command
print x.get_text()
