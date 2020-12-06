sum = 0
cnt = 0
questions = []
for group in open('input.txt', 'r').readlines():
	if group == '\n':
		for x in set(questions):
			if questions.count(x) == cnt:
				sum += 1
		questions = []
		cnt = 0
	else:
		items = list(group.rstrip('\n'))
		cnt += 1
		for item in items:
			questions.append(item)
	
for x in set(questions):
	if questions.count(x) == cnt:
		sum += 1
print(sum)
