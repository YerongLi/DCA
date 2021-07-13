import pymongo
import json
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.dbpedia

document = db.document
js = json.load(open('d.json','r'))
for entry in js:
	if document.find_one({'_id': entry['_id']}):
		title = entry['title'] if 'title' in entry else ''
		document.update_one({'_id': entry['_id']}, {'$set' : {'text' : entry['text'], 'title' : title}})