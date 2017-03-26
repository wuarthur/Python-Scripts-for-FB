import facebook
import json
import time
import sentiment_analysis
import Scrape

pageID = '1687756434851039'
token = 'EAAX4JJPK6jkBACzZAkDVZBZAJHKl6Il5Ly8cAtcVJym0JSwtBXLvptHLgGeZCm6AreELWkcgXqbZCdxlqhpy06IwEUXyUt1dqb3IRE5CdYZBVgB7P7r3Qy6KHx9ytbtiOVI5JDnG5L6bruwWpL6vxfZAqTcXrAEd8oAZAjyHiIQ43KSZC7QtZCxP988wK57JwtDswZD'
pattern = '%Y %m %d %H:%M:%S'
AllPosts = [];
class _Post:
    def __init__(self, id, time, message):
        self.id = id
        self.time = time
        self.message = message
        self.score = 2
        self.category = ''

def parseResponse(_posts):
    jsonString = str(_posts)
    jsonString = jsonString.split('[')
    jsonString = jsonString[1].split(']')
    jsonString = jsonString[0]
    jsonString = "[" + jsonString + "]"
    jsonString = jsonString.replace("'", '"')
    return json.loads(jsonString)



def PopulatePostClass(_posts):
    jsonObject = parseResponse(_posts)
    final = len(jsonObject)
    num=0
    while num<final:
        POST = _Post(jsonObject[num]['id'],jsonObject[num]['created_time'],jsonObject[num]['message'])
        AllPosts.append(POST)
        num += 1


def PostComments():
    for post in AllPosts:
        if post.score < 40:
            graph.put_comment(object_id=post.id, message=Scrape.GetQuotes(post.category) )



def GetScore():
    for post in AllPosts:
        score = sentiment_analysis.getTextAnalysis(post.message)
        post.score = score



graph = facebook.GraphAPI(access_token=token, version='2.7')
attachment =  {
    'name': 'Link name',
    'link': 'https://www.example.com/',
    'caption': 'Check out this example',
    'description': 'This is a longer description of the attachment',
    'picture': 'https://www.example.com/thumbnail.jpg'
}
profile = graph.get_object(pageID)
posts = graph.get_connections(profile['id'], 'posts')

PopulatePostClass(posts)
GetScore()
PostComments()

#graph.put_comment(object_id='1031262963672150_1032927990172314', message='Great post...')



