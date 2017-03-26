import facebook

graph = facebook.GraphAPI(access_token='your_token', version='2.8')
post = graph.get_object(id='post_id')
print(post['message'])