import tqdm
import json
import utils
import os

print(os.path.basename(__file__))
ent_desc = json.load(open('../data/ent2desc.json', 'r'))
voca_emb_dir = "../data/generated/embeddings/word_ent_embs/"

entity_voca, entity_embeddings = utils.load_voca_embs(voca_emb_dir + 'dict.entity',
                                                          voca_emb_dir + 'entity_embeddings.npy')

directdict = {entity.split('/')[-1] : ent_desc [entity_voca.word2id[entity]] for entity in entity_voca.word2id \
		if entity_voca.word2id[entity] in ent_desc}
print(json.dumps(directdict, indent=2))
	