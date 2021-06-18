import tqdm
with open('../data/generated/test_train_data/aida_train.csv') as f:
	dicmention = dict()
	for line in tqdm.tqdm(f):
		l = line.split('\t')
		docid = l[1]
		mention = l[2]
		if docid not in dicmention:
			dicmention[docid] = dict()
		if mention not in dicmention[docid]:
			dicmention[docid][mention] = (l[6:-2], l[-1][:-1])
		(candidates, groundtruth) = dicmention[docid][mention]
		candidates = [c.split(',')[-1] for c in candidates]
		# assert(l[6:-2] == dicmention[docid][mention][0])
		# if not l[6:-2] ==  dicmention[docid][mention][0]:
		# 	# print(l[6:-2])
		# 	# print(dicmention[docid][mention][0])
		# 	# raise AssertionError
		# 	break
	print(dicmention['1 EU)']['German'])