import pymongo
import json
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.dbpedia

document = db.document
