import requests
from bs4 import BeautifulSoup
from lxml import html

path = r"C:\Users\Kolro\Downloads\bcpshighschoolhpg1.html"
with open(path, "r", encoding='utf-8') as file:
	tree = html.fromstring(file.read())
	
count = 1

for i in range(60):
	htmlp = f'/html/body/div[4]/div/div[1]/div[3]/table/tbody/tr[{count}]/td[1]/h5/a/text()'
	name = tree.xpath(htmlp)
	print(name)
	count += 1
