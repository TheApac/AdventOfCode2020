dir = 0
n = 0
e = 0

for instruction in open('input.txt').readlines():
	instruction = instruction.rstrip('\n')
	value = int(instruction[1:])
	if instruction[:1] == 'N':
		n += value
	if instruction[:1] == 'S':
		n -= value
	if instruction[:1] == 'E':
		e += value
	if instruction[:1] == 'W':
		e -= value
	if instruction[:1] == 'R':
		dir += value
		dir = dir % 360
	if instruction[:1] == 'L':
		dir -= value
		if dir < 0:
			dir = 360 + dir
	if instruction[:1] == 'F':
		if dir == 0:
			e += value
		elif dir == 90:
			n -= value
		elif dir == 180:
			e -= value
		elif dir == 270:
			n += value
print(abs(e) + abs(n))