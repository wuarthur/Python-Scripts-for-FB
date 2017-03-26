import json
import pymongo

uri = "mongodb://yiyang:1NkKsp0dEvFHQYqW8erL9Ad16FwXCMijHTZ43gIyHlah9GKl2BGPMO6UhYbSIPdDryu1lv1bF71VSnpbk6GASw==@yiyang.documents.azure.com:10250/?ssl=true&ssl_cert_reqs=CERT_NONE"
client = pymongo.MongoClient(uri)
db = client.test_database
db = client.get_database("Dates")

def Store(_id, _dates):
    post = {"id": _id,
             "date": _dates
             }
    post_id = db.posts.insert_one(post).inserted_id




def Retrieve(_id):
    jsonStr = db.posts.find_one({"id": _id})
    if jsonStr is None:
        return ""
    jsonStr =  str(jsonStr).replace("'",'"').replace("ObjectId",'').replace("(",'').replace(")","")
    jsonObj = json.loads(jsonStr)
    return (jsonObj["date"])

Store("1687756434851039", "11111111" ,"2017-03-26T14:48:31+0000")
print(Retrieve("1687756434851039"))

