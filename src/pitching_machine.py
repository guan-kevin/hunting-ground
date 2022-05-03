print('fixed')
with open('texts/hello.txt', 'r') as f:
	for line in f:
		print(line.rstrip())
