values = []
for line in open('input.txt', 'r').readlines():
	values.append(int(line.rstrip('\n')))

values.sort()

for i in range(len(values)):
	for j in range(len(values) - 1, 0, -1):
		if values[i] + values[j] == 2020:
			print(values[i] * values[j])
		if values[i] + values[j] < 2020:
			break;