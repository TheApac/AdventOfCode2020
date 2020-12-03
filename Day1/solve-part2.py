values = []
for line in open('input.txt', 'r').readlines():
	values.append(int(line.rstrip('\n')))

values.sort()
  
for i in range(0, len(values)-2): 
    for j in range(i + 1, len(values)-1):  
        for k in range(j + 1, len(values)): 
            if values[i] + values[j] + values[k] == 2020: 
                print(values[i]*values[j]*values[k]) 
