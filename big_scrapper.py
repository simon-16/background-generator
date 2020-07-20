from bs4 import BeautifulSoup
import requests
import pprint
from selenium import webdriver

def find_popular_articles(num_pages):
    hn_total = []
    for page in range(1, num_pages +1):
        res = requests.get('https://news.ycombinator.com/news?p=' + str(page))
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        votes = soup.select('.score')
        hn_total.extend(create_custom_hn(links, votes))
    return sort_by_votes(hn_total)

def sort_by_votes(hn_articles):
    print(f' Here are {len(hn_articles)} articles rated equal or better 100 points')
    return sorted(hn_articles, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        try:
            vote = int(votes[idx].getText().split(' ')[0])
            if vote >= 100 :
                hn.insert(idx, {'title': title, 'link':href ,'votes': vote})
        except IndexError:
            print('A index error occured')
    return hn

pprint.pprint(find_popular_articles(2))
