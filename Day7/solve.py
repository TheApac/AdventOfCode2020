bags = dict()
def has_shiny_gold(name):
	if name == 'shiny gold':
		return True
	if len(bags[name]) == 0:
		return False
	return any([r for r in bags[name] if r == 'shiny gold' or has_shiny_gold(r)])


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
		bags[bag_name].add(rule[2:])

cnt = 0
for name, rules in bags.items():
	for rule in rules:
		if has_shiny_gold(rule):
			cnt += 1
			break

print(cnt)