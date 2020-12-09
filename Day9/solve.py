def isValid(numbers, number):
	numbers.sort()
	for num in numbers:
		for j in range(len(numbers) - 1, 0, -1):
			if num + numbers[j] == number:
				return True
			if num + numbers[j] < number:
				break
	return False

numbers = []

for number in open('input.txt', 'r').readlines():
	number = number.rstrip('\n')
	if len(numbers) > 24:
		if not isValid(numbers[-25:], int(number)):
			print(number)
			break
	numbers.append(int(number))