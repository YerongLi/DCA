import pickle
import json

ent_inlinks_path = "../data/entityid_dictid_inlinks_uniq.pkl"



with open(ent_inlinks_path, 'rb') as f_pkl:
	ent_inlinks_dict = pickle.load(f_pkl)

print(ent_inlinks_dict[262048])

ent_desc = json.load(open('../data/ent2desc.json', 'r'))
print(ent_desc.keys())