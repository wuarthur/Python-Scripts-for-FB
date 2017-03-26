import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.brainyquote.com/quotes/topics/topic_positive2")
#data = str(r.text)
#data = data.split('<div id="quotesList" class="new-msnry-grid bqcpx" data-sai-includehighlight="true">')
#print(data[1])

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

quoteTags = soup.findAll('a', { "class" : "b-qt" })

quotes = []
for quote in quoteTags:
    quotes.append(quote.text)

print(quotes[0])