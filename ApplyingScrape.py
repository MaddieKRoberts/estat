from bs4 import BeautifulSoup
import html2text



path = r"C:\Users\Kolro\Downloads\scraping_salaries\ss1.html"
with open(path, "r", encoding='utf-8') as file:
	cont = file.read()

soup = BeautifulSoup(cont, 'html.parser')

tt = soup.find_all('tr')


for t in tt:
	name = t.find('a')
	print(html2text.html2text(newname))