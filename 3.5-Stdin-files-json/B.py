from sys import stdin

lines = []
for line in stdin:
    s = list(line.rstrip("\n").split())
    lines.append(int(s[2]) - int(s[1]))

print(round(sum(lines) / len(lines)))