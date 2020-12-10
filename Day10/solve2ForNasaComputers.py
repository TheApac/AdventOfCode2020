count = 0

def findSol(cur, sub):
	global count
	if len(sub) == 0:
		return True
	for i in range(len(sub)):
		if sub[i] - cur <= 3:
			if findSol(sub[i], sub[i + 1:]):
				count += 1
			else:
				continue
		if sub[i] - cur > 4:
			return False
	return False

adapters = []

for adapter in open('input.txt', 'r').readlines():
	adapter = adapter.rstrip('\n')
	adapters.append(int(adapter))

adapters.sort()
findSol(0, adapters) 
print(count)