f = open('input.txt')
instructions = f.read().split('\n')
mask = ""
bytes = [0]*65458 # Max adress in my given file + 1
for data in instructions:
	if '[' in data:
		adress = int(data[(list(data)).index('[') + 1:(list(data)).index(']')])
		value = data[(list(data)).index('=') + 1:]
		list_bin_value = list(format(int(value), '036b'))
		for n, i in enumerate(list(mask)):
			if i != 'X':
				list_bin_value[n] = i
		bytes[adress] = int("".join(list_bin_value), 2)
	else:
		mask = data[7:]

print(sum(bytes))