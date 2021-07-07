import json
predicions_score = json.load(open('aida-train.json', 'r'))

scores = [[list(pred['pred'].values()) for pred in predicions_score[doc_]] for doc_ in predicions_score]
print(scores)