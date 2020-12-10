count = 0

adapters = []

for adapter in open('input.txt', 'r').readlines():
	adapter = adapter.rstrip('\n')
	adapters.append(int(adapter))

adapters.sort()
memo = [1] + [0]*(adapters[-1])

for adapter in adapters:
	memo[adapter] = memo[adapter-1] + memo[adapter - 2] + memo[adapter - 3]

print(memo[-1])