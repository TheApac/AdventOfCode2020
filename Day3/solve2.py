map = []
i = 0
for line in open('input.txt', 'r').readlines():
	map.append([char for char in line.rstrip('\n')])
	i += 1
		
i = 0
j1 = 0
j2 = 0
j3 = 0
j4 = 0
j5 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
while i < len(map) - 1:
	i += 1
	j1 += 1
	j1 = j1 % len(map[0])
	j2 += 3
	j2 = j2 % len(map[0])
	j3 += 5
	j3 = j3 % len(map[0])
	j4 += 7
	j4 = j4 % len(map[0])
	if i%2 == 0:
		j5 += 1
		j5 = j5 % len(map[0])
	if map[i][j1] == "#":
		cnt1 += 1
	if map[i][j2] == "#":
		cnt2 += 1
	if map[i][j3] == "#":
		cnt3 += 1
	if map[i][j4] == "#":
		cnt4 += 1
	if i%2 == 0 and map[i][j5] == "#":
		cnt5 += 1

print(cnt1*cnt2*cnt3*cnt4*cnt5)