import pymongo
import json
import spacy
import pytextrank
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.dbpedia
nlp = spacy.load("en_core_web_lg")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
document = db.document

for entry in document.find():
		# title = entry['title'] if 'title' in entry else ''
		doc = nlp(entry['text'])
		keywords = [phrase.text for phrase in doc._.phrases]
		print(keywords)
		# document.update_one({'_id': entry['_id']}, {'$set' : {'key1' : entry['text']}})