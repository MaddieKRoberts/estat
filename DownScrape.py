from bs4 import BeautifulSoup
import html2text
import requests

name_list = []

def download_names():
	page = 1
	for i in range(10):
		url = f'https://govsalaries.com/salaries/MD/baltimore-county-public-schools/j/high-school-english?year=2025&page={page}'
		response = requests.get(url)
		path = r'C:\Users\Kolro\Downloads\scraping_salaries\english'
		
		with open(path + f'{page}' + '.html', 'wb') as f:
			f.write(response.content)
		
		page += 1
	
def scrape(subject):
	n = 1
	for i in range(5):
		path = r"C:\\Users\\Kolro\\Downloads\\scraping_salaries\\" + subject + f"{n}.html"
		with open(path, "r", encoding='utf-8') as file:
			cont = file.read()
		
		soup = BeautifulSoup(cont, 'html.parser')
		
		tt = soup.find_all('tr')
	
		for t in tt:
			name = t.find('a')
			#print(name.text) if name else print('')
			try: 
				name_list.append(name.text)
			except Exception as e:
				2+2
		n+=1


subjects = ['history', 'science', 'math', 'english']
for i in subjects:
	scrape(i)
	
print (name_list)

	