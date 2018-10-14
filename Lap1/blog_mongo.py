from pymongo import MongoClient
uri = "mongodb://khanhc4e:khanhdeptrai123@ds225253.mlab.com:25253/c4e1"

#Connect to database
client = MongoClient(uri)
db = client.get_default_database()
#Collection
posts = db["posts"] #insert_one (C), find (R)

post_list = posts.find()
for p in post_list:
    print(p["author"])
    print(p["title"])
    print(p["content"])

#Document
#Create a document
# post = {
#     "title":"Hom nay troi mua",
#     "content":"Toi di choi",
#     "author" : "Khabi"
# }
# #Insert created document
# posts.insert_one(post)
