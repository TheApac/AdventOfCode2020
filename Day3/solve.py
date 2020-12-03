map = []
i = 0
for line in open('input.txt', 'r').readlines():
	map.append([char for char in line.rstrip('\n')])
	i += 1
		
i = 0
j = 0
cnt = 0
while i < len(map) - 1:
	i += 1
	j += 3
	j = j % len(map[0])
	if map[i][j] == "#":
		cnt += 1

print(cnt)
