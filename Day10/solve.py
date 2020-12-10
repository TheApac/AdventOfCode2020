adapters = []

for adapter in open('input.txt', 'r').readlines():
	adapter = adapter.rstrip('\n')
	adapters.append(int(adapter))

one = 0
three = 0
last = 0
adapters.sort()
for adapter in adapters:
	if adapter - last == 1:
		one += 1
	elif adapter - last == 3:
		three += 1
	last = adapter
print(one * (three + 1))