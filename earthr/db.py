import pymongo

mongo = pymongo.MongoClient(, connect=False) #insert string with mongo information

db = pymongo.database.Database(mongo, 'mydatabase')
col = pymongo.collection.Collection(db, 'mycollection')

col_results = json.loads(dumps(#stuff here for col parsing))
