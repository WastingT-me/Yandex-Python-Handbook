n = int(input())
food = set()
for i in range(n):
    food.add(input())
m = int(input())
given_food = set()
for i in range(m):
    k = int(input())
    for i in range(k):
        given_food.add(input())
not_given = food - given_food
if len(not_given) == 0:
    print('Готовить нечего')
else:
    for i in sorted(list(not_given)):
        print(i)