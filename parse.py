with open('../data/generated/test_train_data/aida_train.csv') as f:
	docset = set()
	for line in f:
		l = line.split('\t')
		if l[1] in docset:
			continue
		docset.add(l[0])
		if l[2] == 'German':
			print(l)