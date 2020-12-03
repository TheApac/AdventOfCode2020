cnt = 0
for line in open('input.txt', 'r').readlines():
	min = int(line.split('-')[0])
	max = int(line.split('-')[1].split(' ')[0])
	letter = line.split(' ')[1].split(':')[0]
	password = line.split(' ')[2].rstrip('\n')
	if max >= password.count(letter) >= min:
		cnt += 1
		
print(cnt)