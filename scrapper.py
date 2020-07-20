from bs4 import BeautifulSoup
import requests

main_url = 'https://news.ycombinator.com'
page = requests.get(main_url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all(class_="score"))
result = (soup.find_all('td', 'span'))
#print(page.text)
print(result)

#print(soup.text)