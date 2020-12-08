instructions = []

for instruction in open('input.txt', 'r').readlines():
	instruction.rstrip('\n')
	instructions.append(instruction)

acc = 0
executed = []
i = 0
while True:
	if i in executed:
		break
	executed.append(i)
	command = instructions[i]
	if command[:3] == 'nop':
		i += 1
	elif command[:3] == 'acc':
		acc += int(command[3:])
		i += 1
	else:
		i += int(command[3:])
	

print(acc)