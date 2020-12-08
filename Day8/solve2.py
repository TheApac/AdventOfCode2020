def execProg(instructions):
	acc = 0
	executed = []
	i = 0
	while i < len(instructions):
		if i in executed:
			return
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
	return acc

instructions = []

for instruction in open('input.txt', 'r').readlines():
	instructions.append(instruction.rstrip('\n'))

for i in range(len(instructions)):
	instructions_bis = instructions.copy()
	command = instructions_bis[i]
	if command[:3] == 'nop':
		instructions_bis[i] = 'jmp ' + command[3:]
		if execProg(instructions_bis) != None:
			break
	elif command[:3] == 'jmp':
		instructions_bis[i] = 'nop ' + command[3:]
		if execProg(instructions_bis) != None:
			break