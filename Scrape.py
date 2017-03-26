import requests

r = requests.get("https://www.brainyquote.com/quotes/topics/topic_positive2")
data = str(r.text)
data = data.split('<div id="quotesList" class="new-msnry-grid bqcpx" data-sai-includehighlight="true">')
print(data[1])