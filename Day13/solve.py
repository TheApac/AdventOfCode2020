import math

dep = 0
idSave = 0
min = math.inf

f = open('input.txt')
dep = int(f.readline())
list = f.read().rstrip('\n').split(',')
for id in list:
	if id != 'x':
		time = int(id) * ((dep // int(id)) + 1)
		if time - dep < min:
			idSave = int(id)
			min = time - dep
print(min * idSave)