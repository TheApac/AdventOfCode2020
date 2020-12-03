cnt = 0
for line in open('input.txt', 'r').readlines():
	first = int(line.split('-')[0])
	second = int(line.split('-')[1].split(' ')[0])
	letter = line.split(' ')[1].split(':')[0]
	password = line.split(' ')[2].rstrip('\n')
	if (password[first-1] == letter) ^ (password[second-1] == letter):
		cnt += 1
		
print(cnt)