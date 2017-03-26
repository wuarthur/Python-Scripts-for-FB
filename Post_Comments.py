import facebook
import json
import time

pattern = '%Y %m %d %H:%M:%S'
AllPosts = [];
class _Post:
    def __init__(self, id, time, message):
        self.id = id
        self.time = time
        self.message = message
        self.score = -1.0

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
        if post.score < 0.4:
            graph.put_comment(object_id=post.id, message='posterrrrrr' )


graph = facebook.GraphAPI(access_token='EAAX4JJPK6jkBAM1wlpIlO91jLT7i3g0xoqZBZAVwQnJpRuZCgywA8hnHXuEydeZBGKRGYclOZBmCxYGnrmcuVEBagJkytCsnIcJ63UdZASZB0DZCgsAMxyz5oG9tXWO6wSK2OHEhPpvCMJj1bXJeSZAc35G66n3VCI0yEHxOgNMs26MOhLNQvZADYs4qVvzBErymIZD', version='2.7')
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
#PostComments()

#graph.put_comment(object_id='1031262963672150_1032927990172314', message='Great post...')



