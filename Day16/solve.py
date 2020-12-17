f = open('inputA.txt')
instructions = f.readlines()

valid_numbers = [False] * 1000

i = 0

while instructions[i] != '\n':
	ranges = instructions[i][instructions[i].index(':')+2:].rstrip('\n')
	for j in range(int(ranges[:ranges.index('-')]), int(ranges[ranges.index('-')+1:ranges.index(' or ')]) + 1):
		valid_numbers[j] = True
	ranges = ranges[ranges.index('or ') + 3:]
	for j in range(int(ranges[:ranges.index('-')]), int(ranges[ranges.index('-')+1:]) + 1):
		valid_numbers[j] = True
	i += 1

i += 5

rate = 0

while i < len(instructions):
	for j in instructions[i].split(","):
		if not valid_numbers[int(j)]:
			rate += int(j)
	i += 1
	
print(rate)