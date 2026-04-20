first, second, answer = input(), input(), input()
s1 = set()
s2 = set()
with open(first, encoding='UTF-8') as f:
    for line in f:
        line = line.split()
        for word in line:
            s1.add(word)
    
with open(second, encoding='UTF-8') as s:
    for line in s:
        line = line.split()
        for word in line:
            s2.add(word)

with open(answer, mode='w', encoding='UTF-8') as a:
    a.write('\n'.join(sorted(list(s1 ^ s2))))