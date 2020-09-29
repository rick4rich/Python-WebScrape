import requests
from bs4 import BeautifulSoup
name = input("Give the site you need to scrape: ")
page = requests.get(name)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
input("Press enter to exit: ")
