sum = 0
questions = []
for group in open('input.txt', 'r').readlines():
	if group == '\n':
		sum += len(list(set(questions)))
		questions = []
	else:
		items = list(group.rstrip('\n'))
		for item in items:
			questions.append(item)
	
sum += len(list(set(questions)))
print(sum)