from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))

s = 0
for line in lines:
    s += sum([int(x) for x in list(line.split())])

print(s)