import json
import itertools
datasets = ['aida-train.json', 'aida-A.json', 'aida-B.json']
for dataset in datasets:
	predicions_score = json.load(open(dataset, 'r'))
	def flatten(listOfLists):
		"Flatten one level of nesting"
		return itertools.chain.from_iterable(listOfLists)
	scores = [[list(pred['pred'].values()) for pred in predicions_score[doc_]] for doc_ in predicions_score]
	scores = list(flatten(scores))
	scores = list(flatten(scores))
	scores = [float(s) for s in scores if s != '-100']
	print(max(scores))
	print(min(scores))