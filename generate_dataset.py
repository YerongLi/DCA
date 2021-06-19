import sys
sys.path.insert(0, "../")
import json
import dataset as D
import utils
from pprint import pprint
import pickle as pkl
import time
import tqdm

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
with open('../data/generated/test_train_data/aida_train.csv') as f:
	dicmention = dict()
	count  = 0
	for line in tqdm.tqdm(f):
		l = line.split('\t')
		docid = l[1]
		mention = l[2]
		if docid not in dicmention:
			dicmention[docid] = dict()
		if mention not in dicmention[docid]:
			dicmention[docid][mention] = (l[6:-2], l[-1][:-1])
		(candidates, groundtruth) = dicmention[docid][mention]
		candidates = [c[c.index(',', c.index(',') + 1) + 1:].replace(' ', '_') for c in candidates]
		doc = l[0]
		groundtruth = groundtruth[groundtruth.index(',', groundtruth.index(',') + 1) + 1:].replace(' ', '_')
		assert(l[6:-2] == dicmention[docid][mention][0])
		# for c in candidates:
		# 	if 'en.wikipedia.org/wiki/' + c in entity_voca.word2id:
		# 		count+= 1
				# print('https://en.wikipedia.org/wiki/' + c, count)
		# tmp.append([f'{doc}==={""}',
		# 	f'{l[2]};{na}',
		# 	str([0.0] * 20),
		# 	label,
		# 	csvfile.iloc[i].Mention,
		# 	f'{csvfile.iloc[i].Sentence}--{csvfile.iloc[i].Mention}',
		# 	1,
		# 	0,
		# 	])
		# if 'en.wikipedia.org/wiki/' + groundtruth in entity_voca.word2id:
		# 	count+= 1
		# 	print('https://en.wikipedia.org/wiki/' + groundtruth, count)

		# if not l[6:-2] ==  dicmention[docid][mention][0]:
		# 	# print(l[6:-2])
		# 	# print(dicmention[docid][mention][0])
		# 	# raise AssertionError
		# 	break
	# (candidates, groundtruth) =dicmention['44 SOCCER)']['Sion']
	# candidates = [c[c.index(',', c.index(',') + 1) + 1:] for c in candidates]
	# print(candidates)