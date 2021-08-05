import sys
sys.path.insert(0, "../")
import json
import dataset as D
import utils
from pprint import pprint
import pickle as pkl
import time
import tqdm
import multiprocessing
import pandas as pd
import json
import os
import pickle
import pymongo
import numpy as np
import matplotlib.cm as cm


manager = multiprocessing.Manager()
doclist = manager.list()
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.dbpedia

document = db.document
datadir = '../data/generated/test_train_data'
conll_path = '../data/basic_data/test_datasets'
person_path = '../data/basic_data/p_e_m_data/persons.txt'
voca_emb_dir = "../data/generated/embeddings/word_ent_embs/"
ent_inlinks_path = "../data/entityid_dictid_inlinks_uniq.pkl"

doc2type = pkl.load(open('../data/doc2type.pkl', 'rb'))
entity2type = pkl.load(open('../data/entity2type.pkl', 'rb'))
mtype2id = {'PER':0, 'ORG':1, 'GPE':2, 'UNK':3}
entity_voca, entity_embeddings = utils.load_voca_embs(voca_emb_dir + 'dict.entity',
                                                          voca_emb_dir + 'entity_embeddings.npy')
print('load conll at', datadir)
conll = D.CoNLLDatasetOnly(datadir, conll_path, person_path, 'offset', 'SL')
# print(conll.train['528 SQUASH) 528 SQUASH)'][0].keys())
# print(conll.train['528 SQUASH) 528 SQUASH)'][0]['candidates'])
# print(conll.train['528 SQUASH) 528 SQUASH)'][0]['gold'])
# print(conll.train['528 SQUASH) 528 SQUASH)'][0]['context'])
# print(conll.train['528 SQUASH) 528 SQUASH)'][1]['context'])
# conll.train['528 SQUASH) 528 SQUASH)'][0].keys()
colors = cm.rainbow(np.linspace(0, 1, 4))
tjson = json.load(open('entityType.json', 'r'))
datasets = [('train', conll.train), ('testA', conll.testA), ('testB', conll.testB)]
def generate_csv(dataset):
	global doclist
	(pos, dataset) = dataset
	(name , dictionary) = dataset
	datax, datay, dataz, datak, datac = [], [], [], [], []
	def process(doc):
		mentionlist = []
		pre_doc = doc.split(' ')[0]
		for i, entry in enumerate(dictionary[doc]):
			if i > 100:
				break
			(groundtruth, gtprior, _) = entry['gold']
			# if groundtruth in tjson and not tjson[groundtruth] == 0: continue
			mention = entry['mention']
			mtype = entry['mtype'].index(1)
			# gttype = gttype.index(1)

			# print(entry.keys())
			mentionlist.append([mention, groundtruth])
			has_groundTruth = False
			statistics = [0]*4
			gttype = 3
			if len(entry['candidates']) == 0: continue
			for candidate in entry['candidates']:
			# for candidate in entry['candidates'][:10]:
				c = candidate[0]
				cname = c.replace('_', ' ')
				ctype = candidate[2].index(1)
				statistics[ctype] += 1
				# typematch = 1 if c == groundtruth or ctype == mtype else 0
				if c == groundtruth:
					gttype = candidate[2].index(1)
					# if gttype != mtype:
					# 	print('mismatch ',gttype, mtype)
					# 	print(mention, groundtruth)
				# # # print(candidate)
				# # # if groundtruth == 'Swansea_City_A.F.C.':
				# # 	# print(c, c == groundtruth, groundtruth)
				# # if (not c == groundtruth) and 'en.wikipedia.org/wiki/' + c not in entity_voca.word2id:
				# # 	continue
				# featurev = [0.0] * 27
				# featurev[16] = candidate[1]
				# featurev[9] = typematch
				# # print(doc)
				# # print(pre_doc)
				# # print(entry["context"])
				# # print(mention)
				# # sys.exit()
				# if c == groundtruth: has_groundTruth = True

				# data.append([f'{entry["context"][0]}',
				# 	f'{mention}==={cname}',
				# 	str(featurev),
				# 	1 if c == groundtruth else 0,
				# 	mention,
				# 	f'{pre_doc} {i} {entry["context"][0]} {entry["context"][1]}--{mention}',
				# 	1,
				# 	0,
				# 	entry["context"][1],
				# 	pre_doc,
				# 	])
			# if not has_groundTruth:
			# 	featurev = [0.0] * 27
			# 	# print(gtprior)
			# 	featurev[16] = gtprior
			# 	featurev[9] = typematch
			# 	# if mention == 'Swansea':
			# 	# 	print(doc, mention)
			# 	# 	print('gold', entry['gold'])
			# 	data.append([f'{entry["context"][0]}',
			# 	f'{mention}==={groundtruth.replace("_", " ")}',
			# 	str(featurev),
			# 	1,
			# 	mention,
			# 	f'{pre_doc} {i} {entry["context"][0]} {entry["context"][1]}--{mention}',
			# 	1,
			# 	0,
			# 	entry["context"][1],
			# 	pre_doc,
			# 	])
			s = sum(statistics)
			data
			# print(s, statistics)
			from mpl_toolkits.mplot3d import Axes3D
			import matplotlib.pyplot as plt

			fig = plt.figure()
			ax = fig.add_subplot(111, projection='3d')
			datax.append(statistics[0]/s)
			datay.append(statistics[1]/s)
			dataz.append(statistics[2]/s)
			datak.append(statistics[3]/s)
			datac.append(colors[gttype])
		# print(data)
		img = ax.scatter(datax, datay, dataz, c=datac, cmap=plt.hot())
		plt.savefig(f'{name}.png')
		# doclist.append({'_id': pre_doc, 'mention': mentionlist, 'set' : 'aida'})
	for doc in tqdm.tqdm(list(dictionary.keys()), position = pos):
		process(doc)
	# df = pd.DataFrame(data, columns=['left','Mention_label','Features','Label','Mention','QuestionMention','db','blink','right','Question'])
	# df.to_csv(f'full_{name}.csv', index = False)
	
	
print('Generating data vector')
with multiprocessing.Pool(3) as pool: 
	pool.map(generate_csv, enumerate(datasets[:1]))
# document.insert_many(list(doclist))
# with open('../data/generated/test_train_data/aida_train.csv') as f:
# 	dicmention = dict()
# 	count  = 0
# 	for line in tqdm.tqdm(f):
# 		l = line.split('\t')
# 		docid = l[1]
# 		mention = l[2]
# 		if docid not in dicmention:
# 			dicmention[docid] = dict()
# 		if mention not in dicmention[docid]:
# 			dicmention[docid][mention] = (l[6:-2], l[-1][:-1])
# 		(candidates, groundtruth) = dicmention[docid][mention]
# 		candidates = [c[c.index(',', c.index(',') + 1) + 1:].replace(' ', '_') for c in candidates]
# 		doc = l[0]
# 		groundtruth = groundtruth[groundtruth.index(',', groundtruth.index(',') + 1) + 1:].replace(' ', '_')
# 		assert(l[6:-2] == dicmention[docid][mention][0])
# 		# for c in candidates:
# 		# 	if 'en.wikipedia.org/wiki/' + c in entity_voca.word2id:
# 		# 		count+= 1
# 				# print('https://en.wikipedia.org/wiki/' + c, count)
# 		# tmp.append([f'{doc}==={""}',
# 		# 	f'{l[2]};{na}',
# 		# 	str([0.0] * 20),
# 		# 	label,
# 		# 	csvfile.iloc[i].Mention,
# 		# 	f'{csvfile.iloc[i].Sentence}--{csvfile.iloc[i].Mention}',
# 		# 	1,
# 		# 	0,
# 		# 	])
# 		# if 'en.wikipedia.org/wiki/' + groundtruth in entity_voca.word2id:
# 		# 	count+= 1
# 		# 	print('https://en.wikipedia.org/wiki/' + groundtruth, count)

# 		# if not l[6:-2] ==  dicmention[docid][mention][0]:
# 		# 	# print(l[6:-2])
# 		# 	# print(dicmention[docid][mention][0])
# 		# 	# raise AssertionError
# 		# 	break
# 	# (candidates, groundtruth) =dicmention['44 SOCCER)']['Sion']
# 	# candidates = [c[c.index(',', c.index(',') + 1) + 1:] for c in candidates]
# 	# print(candidates)