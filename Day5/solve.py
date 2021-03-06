def getId(code):
	rowL = 0
	rowH = 127
	for i in range(7):
		if code[i] == 'F':
			rowH = rowH - int((rowH-rowL+1)/2)
		else:
			rowL = rowL + int((rowH-rowL+1)/2)
	colL = 0
	colH = 7
	for i in range(7, 10):
		if code[i] == 'L':
			colH = colH - int((colH-colL+1)/2)
		else:
			colL = colL + int((colH-colL+1)/2)
	return rowL * 8 + colL

higher = 0
for line in open('input.txt', 'r').readlines():		
	higher = max(higher, getId(line))

print(higher)