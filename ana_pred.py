import json
import itertools
predicions_score = json.load(open('aida-train.json', 'r'))
def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)
scores = [[list(pred['pred'].values()) for pred in predicions_score[doc_]] for doc_ in predicions_score]
scores = list(flatten(scores))
scores = list(flatten(scores))
scores = [float(s) if s != '-100' for s in scores]
print(scores)