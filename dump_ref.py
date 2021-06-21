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
datasets = [('train', conll.train), ('testA', conll.testA), ('testB', conll.testB)]
m = multiprocessing.Manager()
resjon = m.dict()
def dump(dataset):
	global resjson
	(pos, dataset) = dataset
	(name , dictionary) = dataset

	for doc in tqdm.tqdm(list(dictionary.keys())):
		for entry in dictionary[doc]:
			(groundtruth, _, _) = entry['gold']
			mention = entry['mention']
			for candidate in entry['candidates']:
				c, ref_count, tipe = candidate[0], candidate[1], candidate[2].index(1)
				print(ref_count, tipe)
				# print(candidate)
				if c not in resjon: resjon[c] = [ref_count, tipe]
				assert(ref_count == resjon[c][0])
				assert(tipe == resjon[c][1])
	# for doc in tqdm.tqdm(list(dictionary.keys()), position = pos):
	# 	process(doc)
	# df = pd.DataFrame(data, columns=['Question','Mention_label','Features','Label','Mention','QuestionMention','db','blink'])
	# df.to_csv(f'full_{name}.csv', index = False)
print(resjon)
with multiprocessing.Pool(3) as pool: 
	pool.map(dump, enumerate(datasets))
with open('refCount.json', 'w') as fp:
    json.dump(resjon, fp)