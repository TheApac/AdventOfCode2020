bags = dict()

def count_shiny_gold(name, nb):
	n = 0
	if len(bags[name]) == 0:
		return nb
	for bag in bags[name]:
		n += nb * int(count_shiny_gold(bag[2:], int(bag[:2])))
	return n + nb


for rule in open('input.txt', 'r').readlines():
	rule.rstrip('\n')
	rule = rule.replace('.', '')
	bag_name = rule.split(' contain')[0].replace(' bags', '')
	bags[bag_name] = set()
	rules = rule.split('contain ')[1]
	if 'no other' in rules:
		continue
	rules = rules.replace('bags', 'bag')
	rule_list = rules.split(' bag')
	for i in range(len(rule_list) - 1):
		rule = rule_list[i]
		rule = rule.replace(', ', '')
		bags[bag_name].add(rule)

print(count_shiny_gold('shiny gold', 1) - 1)