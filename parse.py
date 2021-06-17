with open('../data/generated/test_train_data/aida_train.csv') as f:
	dicmention = dict()
	for line in f:
		l = line.split('\t')
		docid = l[1]
		mention = l[2]
		if docid not in dicmention:
			dicmention[docid] = dict()
		if mention not in dicmention[docid]:
			dicmention[docid][mention] = (l[5:-2], l[-1])
		assert l[5:-2] ==  dicmention[docid][mention][0]
	print(dicmention['1 EU)']['German'])