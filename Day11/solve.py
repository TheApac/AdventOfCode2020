import copy

seats = []

def countSeats(x, y):
	nb = 8
	if seats[x-1][y-1] == '#':
		nb -= 1
	if seats[x][y-1] == '#':
		nb -= 1
	if seats[x+1][y-1] == '#':
		nb -= 1
	if seats[x-1][y] == '#':
		nb -= 1
	if seats[x+1][y] == '#':
		nb -= 1
	if seats[x][y+1] == '#':
		nb -= 1
	if seats[x-1][y+1] == '#':
		nb -= 1
	if seats[x+1][y+1] == '#':
		nb -= 1
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
			if seats[i][j] == '#' and countSeats(i,j) < 5:
				seatsCopy[i][j] = 'L'
				modified = True
	seats = copy.deepcopy(seatsCopy)

cnt = 0
for i in range(1, len(seats) - 1):
	for j in range(1, len(seats[i]) - 1):
		if seats[i][j] == '#':
			cnt += 1
			
print(cnt)