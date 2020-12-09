numbers = []
answer = 248131121 # Answer given by solve.py for first part

for number in open('input.txt', 'r').readlines():
	number = number.rstrip('\n')
	numbers.append(int(number))

for i in range(len(numbers)):
	number = numbers[i]
	cur = number
	j = i + 1
	while j < len(numbers): 
		if number > answer or j == len(numbers): 
			break
		cur = cur + numbers[j]
		if cur == answer and number != answer: 
			print(min(numbers[i:j+1]) + max(numbers[i:j+1])) 
			i = len(numbers)
			break
		j += 1