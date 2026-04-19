from itertools import product

s = ['пик', 'треф', 'бубен', 'червей']
n = input()
s = [i for i in s if i != n]

for i, v in product([2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'], s):
    print(i, v)