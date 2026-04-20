N, M, Q, cw, sw, hw, tw = map(int, input().split())
if (not M > 0) or (not cw > 0) or (not sw > 0) or (not hw > 0) or (not tw > 0):
    print("Во введённых данных ошибка")
else:
    for i in range(1):
        last_name = input()
        s = 0
        for j in range(M):
            a, b, c, d = map(int, input().split(","))
            s = s + a * cw + b * sw + c * hw + d * tw
        if s > Q:
            print("Во введённых данных ошибка")
        else:
            print(f"{last_name} {round(s / Q * 100)}%")