from math import prod

f = open("input.txt")
f.readline()
list_bus = []
buses = f.readline().split(',')
list_bus = [(bus_id, int(x)) for bus_id, x in enumerate(buses) if x != "x"]
eucl = lambda a, b: 0 if a == 0 else 1 if b % a == 0 else b - eucl(b % a, a) * b // a
N = prod([bus[1] for bus in list_bus])
x = sum([bus[0] * (N // bus[1]) * eucl(N // bus[1], bus[1]) for bus in list_bus])
print(N - x % N)