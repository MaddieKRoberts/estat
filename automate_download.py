import requests


page = 1
for i in range(10):
	url = f'https://govsalaries.com/salaries/MD/baltimore-county-public-schools/j/high-school-social-studies?year=2025&page={page}'
	response = requests.get(url)
	path = r'C:\Users\Kolro\Downloads\scraping_salaries\ss'
	with open(path + f'{page}' + '.html', 'wb') as f:
		f.write(response.content)
	page += 1
#https://govsalaries.com/salaries/MD/baltimore-county-public-schools/j/high-school-social-studies?year=2025
#https://govsalaries.com/salaries/MD/baltimore-county-public-schools/j/high-school-social-studies?year=2025&page=2