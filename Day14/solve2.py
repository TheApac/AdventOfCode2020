def replaceX(list_val, values):
	if 'X' not in list_val:
		return values.append(int("".join(list_val), 2))
	else:
		str_val = ''.join(list_val)
		copy = list(str_val)
		copy[str_val.rindex('X')] = '0'
		with_zero = copy
		copy = list(str_val)
		copy[str_val.rindex('X')] = '1'
		with_one = copy
		replaceX(with_zero, values)
		replaceX(with_one, values)
		return values

f = open('input.txt')
instructions = f.read().split('\n')
mask = ""
bytes = dict() # Max adress in my given file + 1
for data in instructions:
	if '[' in data:
		adress = int(data[(list(data)).index('[') + 1:(list(data)).index(']')])
		value = data[(list(data)).index('=') + 1:]
		list_adress = list(format(int(adress), '036b'))
		for n, i in enumerate(list(mask)):
			if i == '1':
				list_adress[n] = '1'
			if i == 'X':
				list_adress[n] = 'X'
		list_adress = replaceX(list_adress, [])
		for ad in list_adress:
			bytes[ad] = int(value)
	else:
		mask = data[7:]

print(sum(bytes.values()))