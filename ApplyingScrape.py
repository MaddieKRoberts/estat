import requests
from bs4 import BeautifulSoup
from lxml import html



path = r"C:\Users\Kolro\Downloads\scraping_salaries\ss1.html"
with open(path, "r", encoding='utf-8') as file:
	tree = html.fromstring(file.read())
	print(tree)
		
count = 1
	
for i in range(60):
	htmlp = f'/script/h3[{count}]/text()'
	name = tree.xpath(htmlp)
	print(name)
	count += 1
