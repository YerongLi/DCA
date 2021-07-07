import json
predicions_score = json.load(open('aida-train.json', 'r'))

scores = [pred['pred'] for pred in predicions_score[doc] for doc in predicions_score]
print(scores)