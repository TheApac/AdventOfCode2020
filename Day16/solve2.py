def find_right_order(possible_list, order, index):
	if index == 20:
		return order
	for possible_solution in possible_list[0]:
		if possible_solution not in order:
			order[index] = possible_solution
			res = find_right_order(possible_list[1:], order, index + 1)
			if res:
				return res
		order[index] = -1
	return False


f = open('inputA.txt')
instructions = f.readlines()

valid_numbers = [False] * 1000
valid_numbers_fields = []

i = 0

while instructions[i] != '\n':
	valid_numbers_field = [False] * 1000
	ranges = instructions[i][instructions[i].index(':')+2:].rstrip('\n')
	for j in range(int(ranges[:ranges.index('-')]), int(ranges[ranges.index('-')+1:ranges.index(' or ')]) + 1):
		valid_numbers_field[j] = True
		valid_numbers[j] = True
	ranges = ranges[ranges.index('or ') + 3:]
	for j in range(int(ranges[:ranges.index('-')]), int(ranges[ranges.index('-')+1:]) + 1):
		valid_numbers_field[j] = True
		valid_numbers[j] = True
	valid_numbers_fields.append(valid_numbers_field)
	i += 1

valid_tickets = []

i += 2

my_ticket = instructions[i].split(",")

valid_tickets.append(instructions[i])

i += 3

valid = True

while i < len(instructions):
	valid = True
	for j in instructions[i].split(","):
		if not valid_numbers[int(j)]:
			valid = False
	if valid:
		valid_tickets.append(instructions[i])
	i += 1

possible_order = []

i = 0

while i < len(valid_numbers_fields):
	possible_order.append([])
	test = 0
	while test < len(valid_numbers_fields):
		valid = True
		for ticket in valid_tickets:
			if not valid_numbers_fields[i][int(ticket.split(',')[test])]:
				valid = False
				break
		if valid:
			possible_order[i].append(test)
		test += 1
	i += 1

right_order = [-1] * len(possible_order)

right_order = find_right_order(possible_order, right_order, 0)
total = 1
for pos in right_order[:6]:
	total *= int(my_ticket[pos])
print(total)
