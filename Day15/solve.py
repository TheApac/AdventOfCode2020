numbers = [0,1,5,10,3,12,19]
mem = {}
for i in range(len(numbers) - 1):
	mem[numbers[i]] = i

for i in range(len(numbers) - 1,30000000 - 1):
	last = numbers[i]
	numbers.append(i - mem[last] if last in mem else 0)
	mem[last] = i
	if i == 2018:
		print("Part 1 : " + str(numbers[-1]))
		
print("Part 2 : " + str(numbers[-1]))