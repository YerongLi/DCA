import pandas as pd
# datasets = [('train', conll.train), ('testA', conll.testA), ('testB', conll.testB)]

df_ = pd.read_csv('full_testA.csv')

n, l, r = df_.shape[0], 0, 0

# try:
while r < n:
	while r < n - 1 and df_.iloc[l]['QuestionMention'] == df_.iloc[r + 1]['QuestionMention']:
		r+= 1
	batch = df_.iloc[l : r + 1]
	gt = batch[batch.Label.eq(1)]
	# print(gt)
	gtn = gt.Mention_label.values[0].split(';')[1]
	print(gtn)
	features = df_.features
	# # assert(len(gold_pairs) == 1)
	# gt = gt[0].split(';')[1].replace(' ', '_')
	# # j = torch.argmax(pred_[l:r + 1]).numpy()
	# # print(j)
	# if j != r - l:
	# 	data.append([df_.iloc[l]['QuestionMention'],
	# 	f'https://dbpedia.org/page/{gt}', 
	# 	f"https://dbpedia.org/page{batch.iloc[j]['Mention_label'].split(';')[1].replace(' ', '_')}"])
	l = r + 1
	r = l
# 	error_df =  pd.DataFrame(data, columns = ['QuestionMention','gold','pred'])
# 	error_df.to_csv('error.csv', index=False)
# except:
	# pass