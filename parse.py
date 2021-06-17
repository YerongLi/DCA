with open('../data/generated/test_train_data/aida_train.csv') as f:
	for line in f:
		print(line.split('\t'))
		break