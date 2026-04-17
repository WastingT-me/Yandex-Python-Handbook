N, M, Q, cw, sw, hw, tw = map(int, input().split())
if (N < 3) or (not M > 0) or (not cw > 0) or (not sw > 0) or (not hw > 0) or (not tw > 0):
    print("Во введённых данных ошибка")
else:
    max_, mean_ = 0, 0
    min_ = Q
    last_name_1, last_name_2, last_name_3 = "", "", ""
    rating_1, rating_2, rating_3 = 0, 0, 0
    for i in range(N):
        last_name = input()
        s = 0
        for j in range(M):
            a, b, c, d = map(int, input().split(","))
            s = s + a * cw + b * sw + c * hw + d * tw
        mean_ += s
        if min_ > s:
            min_ = s
        if max_ < s:
            max_ = s
        if rating_1 < s:
            last_name_3 = last_name_2
            rating_3 = rating_2

            last_name_2 = last_name_1
            rating_2 = rating_1

            last_name_1 = last_name
            rating_1 = s
        elif rating_2 < s:
            last_name_3 = last_name_2
            rating_3 = rating_2

            last_name_2 = last_name
            rating_2 = s
        elif rating_3 < s:
            last_name_3 = last_name
            rating_3 = s
    if rating_1 > Q:
        print("Во введённых данных ошибка")
    else:
        print(round(max_ / Q * 100), round(mean_ / N / Q * 100), round(min_ / Q * 100))        
        print(last_name_1, f"{round(rating_1 / Q * 100)}%")   
        print(last_name_2, f"{round(rating_2 / Q * 100)}%")
        print(last_name_3, f"{round(rating_3 / Q * 100)}%")
        if mean_ / N / Q * 100 > 50:
            print("Курс усваивается хорошо") 
        else:
            print("Курс усваивается плохо") 