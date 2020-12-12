n = 0
e = 0
nW = 1
eW = 10

for instruction in open('input.txt').readlines():
	instruction = instruction.rstrip('\n')
	value = int(instruction[1:])
	if instruction[:1] == 'N':
		nW += value
	if instruction[:1] == 'S':
		nW -= value
	if instruction[:1] == 'E':
		eW += value
	if instruction[:1] == 'W':
		eW -= value
	if instruction[:1] == 'R':
		for i in range(value // 90):
			nW, eW = -eW, nW
	if instruction[:1] == 'L':
		for i in range(value // 90):
			nW, eW = eW, -nW
	if instruction[:1] == 'F':
		n += nW * value
		e += eW * value
print(abs(e) + abs(n))