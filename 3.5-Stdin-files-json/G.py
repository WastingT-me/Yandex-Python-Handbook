path = input()
count, count_pos, min_number, max_number, sum_all = 0, 0, float('inf'), float('-inf'), 0
with open(path, encoding="UTF-8") as file_in:
    for line in file_in:
        line = list(map(int, line.split()))
        count += len(line)
        count_pos += len([i for i in line if i > 0])
        min_number = min(min_number, min(line))
        max_number = max(max_number, max(line))
        sum_all += sum(line)

print(f'{count}\n{count_pos}\n{min_number}\n{max_number}\n{sum_all}\n{sum_all / count:.02f}')