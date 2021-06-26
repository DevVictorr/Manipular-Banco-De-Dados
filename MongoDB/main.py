from pymongo import MongoClient, collection
import datetime

conn = MongoClient('Localhost',27017)



db = conn.cadastrodb

collection = db.cadastrodb


post1 = {
            "codigo"   :"ID-994213",
            "prod_name":"Geladeira",
            "marcas"   :"bastemp",
            "cadastro" :datetime.datetime.utcnow()
}

collection = db.posts

post_id = collection.insert_one(post1)


post_id.inserted_id
print(post_id)
post2 = {
            "codigo"   :"ID-932113",
            "prod_name":"Carro",
            "marcas"   :"Ford",
            "cadastro" :datetime.datetime.utcnow()
}

collection = db.posts

post_id = collection.insert_one(post2).inserted_id

print(post_id)

for post in collection.find():
    print(post)