import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
	# делаем запрос по адресу и получаем ответ
	resp = requests.get(url)
	return resp.text

def get_soup(html):
	soup = BS(html, 'lxml')
	return soup

def get_date(soup):
	#       код html и название парсера
	date = soup.find('div',class_ = 'row hidden-xs').find('h3').get_text()
	return date

def get_titles(soup):
	items = soup.find('div', class_ = 'col-xs-8').find_all('div', class_ = 'show')
	titles = []
	for item in items:
		title = item.find('p', class_ = 'show-title').get_text()
		titles.append(title)
	return titles

def main():
	url = 'https://www.ts.kg/'	
	# print(get_html(url))
	html = get_html(url)# получаем исходный код страницы
	soup = get_soup(html)# получаем объект BS	
	date = get_date(soup)# парсим дату со страницы  
	titles = get_titles(soup)# парсим названия сериалов
	print(date)
	print(*titles, sep = '\n')

if __name__ == '__main__':
	main()
