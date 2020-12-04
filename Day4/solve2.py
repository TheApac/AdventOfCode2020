import string;

cnt = 0
for passport in open('inputClarified.txt', 'r').readlines():
	elems = passport.split(' ')
	elems.sort()
	v = True
	for elem in elems:
		elem = elem.rstrip('\n')
		if 'byr' in elem and not 1920 <= int(elem[4:]) <= 2002:
			v = False
		if 'iyr' in elem and not 2010 <= int(elem[4:]) <= 2020:
			v = False
		if 'eyr' in elem and not 2020 <= int(elem[4:]) <= 2030:
			v = False
		if 'hgt' in elem and (not (elem[-2:] == 'cm' or elem[-2:] == 'in') or not elem[4:][:-2].isnumeric() or not ((elem[-2:] == 'cm' and 150 <= int(elem[4:][:-2]) <= 193) or (elem[-2:] == 'in' and 59 <= int(elem[4:][:-2]) <= 76))):
			v = False
		if 'hcl' in elem and (all(c in string.hexdigits for c in elem[4:][:-1]) and elem[4:][:-6] != '#'):
			v = False
		if 'ecl' in elem and ((len(elem[4:]) != 3 or elem[4:] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
			v = False
		if 'pid' in elem and (len(elem[4:]) != 9 or not elem[4:].isnumeric()):
			v = False
	if v:
		cnt += 1
print(cnt)