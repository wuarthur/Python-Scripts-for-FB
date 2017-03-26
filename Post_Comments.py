import facebook
import json
import time
import sentiment_topic_analysis

token = 'EAAX4JJPK6jkBABWBzCB3UsVbT2vqdFLGMCRqIS2Q2CDZCQFW6bRafFc9hxJgWH28uX5X96mdWqZBIRoIwZBNkAZA2VfiYX2lhFq4rMlGVA2PjFU94B9ZAZCBioZA4aXDoqN2VzKj73vBU299aiIOt5BSgz3W22JKbqVyKi235aiMxN8GqpA2l0iTNCEsAIgE58ZD'
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
            graph.put_comment(object_id=post.id, message='this is under 22' )


def GetScore():
    for post in AllPosts:
        score = sentiment_topic_analysis.GetAnaly(post.message)
        post.score = score



graph = facebook.GraphAPI(access_token=token, version='2.7')
attachment =  {
    'name': 'Link name',
    'link': 'https://www.example.com/',
    'caption': 'Check out this example',
    'description': 'This is a longer description of the attachment',
    'picture': 'https://www.example.com/thumbnail.jpg'
}
profile = graph.get_object("1031262963672150")
posts = graph.get_connections(profile['id'], 'posts')

PopulatePostClass(posts)
GetScore()
PostComments()

#graph.put_comment(object_id='1031262963672150_1032927990172314', message='Great post...')



