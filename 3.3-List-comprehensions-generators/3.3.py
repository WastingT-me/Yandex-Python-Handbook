# A
# [x ** 2 for x in range(a, b + 1)]

# O
# {char: text.lower().count(char) for char in ''.join(s for s in text.lower() if s.isalnum())}

# P RLE reverse
# str(''.join([a * b for (a, b) in rle]))

# Q
# [[k * i for i in range(1, n + 1)] for k in range(1, n + 1)]

# O Divisors
# {i: div for i, div in [(i, [j for j in range(1, i + 1) if i % j == 0]) for i in numbers]}

# S
# set([i for i in numbers if 0 not in [i % j for j in range(2, i)] and i != 1])

# T
# set([(min(a, b), max(a, b)) for a in text.split() for b in text.split() if (len(set(a) & set(b)) > 2 and a != b)])