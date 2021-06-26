import pymongo


conn = pymongo.MongoClient()



db = conn.cadastrodb

#db.create_collection("mycollection")

db.mycollection.insert_one({
   'titulo'    :'mongoDB at Python',
    'descricao' :'Banco de dados',
    'likes'     : 100
    })

print(db.mycollection.find_one())
