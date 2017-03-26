import requests
from bs4 import BeautifulSoup

def GetQuotes(Category):
    topic='positive'
    pageNum=1
    quotes = []
    if Category!='':
        topic=Category
    while pageNum <= 10:
        r = requests.get("https://www.brainyquote.com/quotes/topics/topic_" + topic + str(pageNum))
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        quoteTags = soup.findAll('a', { "class" : "b-qt" })
        for quote in quoteTags:
            quotes.append(quote.text)
        pageNum += 1
        return quotes

GetQuotes("")