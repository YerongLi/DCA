import pandas as pd
import multiprocessing
datasets = ['full_train.csv', 'full_testA.csv', 'full_testB.csv']
def check(filename):
	df = pd.read_csv(filename)
	n, l, r = df.shape[0], 0, 0
	data = []
	# print(df_.shape, 'shape')
	while r < n:
		while r < n - 1 and df.iloc[l]['QuestionMention'] == df.iloc[r + 1]['QuestionMention']:
			r+= 1
		batch = df.iloc[l : r + 1]
		ground_truth = batch[batch.Label.eq(1)]
		if ground_truth.shape[0] != 1:
			print(ground_truth)
with multiprocessing.Pool(3) as p:
	p.map(check, datasets)