import pandas as pd
import tqdm
import multiprocessing
datasets = [(0, 'full_train.csv'), (1, 'full_testA.csv'), (2, 'full_testB.csv')]
def check(filename):
	position, filename = filename
	df = pd.read_csv(filename)
	n, l, r = df.shape[0], 0, 0
	pbar = tqdm.tqdm(total = len(set(df.QuestionMention.values.tolist())), position=position)
	# print(df_.shape, 'shape')
	while r < n:
		while r < n - 1 and df.iloc[l]['QuestionMention'] == df.iloc[r + 1]['QuestionMention']:
			r+= 1
		batch = df.iloc[l : r + 1]
		ground_truth = batch[batch.Label.eq(1)]
		pbar.update(1)
		if ground_truth.shape[0] != 1:
			print(ground_truth.shape[0])
	pbar.update
with multiprocessing.Pool(3) as p:
	p.map(check, datasets)