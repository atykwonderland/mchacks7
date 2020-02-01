import pymongo
from flask import jsonify

mongo = pymongo.MongoClient("mongodb+srv://alice:alice123@cluster0-bd4ay.mongodb.net/test?retryWrites=true&w=majority", connect=False) #insert string with mongo information
db = mongo.test
#db = pymongo.database.Database(mongo, 'mydatabase')
col = db.earthr
data = [food for food in col.find()]

