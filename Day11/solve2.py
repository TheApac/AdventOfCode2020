import copy

seats = []

def countSeats(x, y):
	nb = 8
	memX = x
	memY = y
	lenSeats = len(seats) - 1
	lenRow = len(seats[0]) - 1
	while x > 0 and y > 0:
		x -= 1
		y -= 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while x > 0:
		x -= 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while x > 0 and y < lenRow:
		x -= 1
		y += 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while y < lenRow:
		y += 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while x < lenSeats and y < lenRow:
		x += 1
		y += 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while x < lenSeats:
		x += 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while x < lenSeats and y > 0:
		x += 1
		y -= 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	x = memX
	y = memY
	while y > 0:
		y -= 1
		if seats[x][y] == '#':
			nb -= 1
			break
		if seats[x][y] == 'L':
			break
	return nb

for line in open('input.txt').readlines():
	seats.append(list('.' + line.rstrip('\n')+ '.'))
	
seats.insert(0, ['.']*len(seats[0]))
seats.append(['.']*len(seats[0]))

modified = True
while modified:
	seatsCopy = copy.deepcopy(seats)
	modified = False
	for i in range(1, len(seats) - 1):
		for j in range(1, len(seats[i]) - 1):
			if seats[i][j] == 'L' and countSeats(i,j) == 8:
				seatsCopy[i][j] = '#'
				modified = True
			if seats[i][j] == '#' and countSeats(i,j) < 4:
				seatsCopy[i][j] = 'L'
				modified = True
	seats = copy.deepcopy(seatsCopy)

cnt = 0
for i in range(1, len(seats) - 1):
	for j in range(1, len(seats[i]) - 1):
		if seats[i][j] == '#':
			cnt += 1
			
print(cnt)