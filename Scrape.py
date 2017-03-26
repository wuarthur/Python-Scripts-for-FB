from random import randint

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


    comment = "You seem a little down, here's a positive quote to lift your spirits:" + "\n" + "\n" + "\""
    comment += quotes[randint(0, len(quotes))] + "\"" + "\n" + "\n" + "If you need someone to talk to, feel free to message me!"
    return comment
GetQuotes("")