import pickle
import json
import utils
import os

ent_inlinks_path = "../data/entityid_dictid_inlinks_uniq.pkl"



with open(ent_inlinks_path, 'rb') as f_pkl:
	ent_inlinks_dict = pickle.load(f_pkl)

print(ent_inlinks_dict[262048])

ent_desc = json.load(open('../data/ent2desc.json', 'r'))
print(ent_desc['Germany'])

voca_emb_dir = "../data/generated/embeddings/word_ent_embs/"


entity_voca, entity_embeddings = utils.load_voca_embs(voca_emb_dir + 'dict.entity',
                                                          voca_emb_dir + 'entity_embeddings.npy')
														  
i = entity_voca.word2id['Berlin']
print(os.getenv("HOME"))
print(entity_voca.id2word[i], 'original')
print(ent_inlinks_dict[i])
for j in ent_inlinks_dict[i]:
	print(entity_voca.id2word[j])
print(ent_inlinks_dict[i])