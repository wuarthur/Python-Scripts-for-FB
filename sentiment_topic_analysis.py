import http.client, urllib.request, urllib.parse, urllib.error, base64, json, requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '8f75c4b05dfd44de81b80ea5b5928a37',
    'Content-Type': 'application/json',
    'Accept': 'application/json'

}

params = urllib.parse.urlencode({
})

input = "test"

body = {
    "documents": [
    {
      "Ocp-Apim-Subscription-Key": "8f75c4b05dfd44de81b80ea5b5928a37",
      "language": "en",
      "id": "1",
      "text": input
    }
  ]
}

url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
r = requests.post(url, data=json.dumps(body), headers=headers)
print(r.text)