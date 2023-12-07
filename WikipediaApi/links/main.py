import requests
from bs4 import BeautifulSoup


START = "Cheese"
URL = "https://en.wikipedia.org/wiki/{START}?action=render"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(page.text)





