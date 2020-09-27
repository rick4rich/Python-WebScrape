import requests, os
from bs4 import BeautifulSoup
name = input("Give the site you need to scrape: ")
cont = 'hello';
URL = 'https://mt4guru.com'
page = requests.get(name)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
input("Press enter to exit: ")
