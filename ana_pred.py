import json
import itertools
predicions_score = json.load(open('aida-train.json', 'r'))
def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)
scores = [[list(pred['pred'].values()) for pred in predicions_score[doc_]] for doc_ in predicions_score]
scores = flatten(scores)
scores = flatten(scores)
print(scores)