import json
path, js = input(), input()
count, count_pos, min_number, max_number, sum_all = 0, 0, float('inf'), float('-inf'), 0
with open(path, encoding="UTF-8") as file_in:
    for line in file_in:
        if not line.strip():
            continue
        line = list(map(int, line.split()))
        count += len(line)
        count_pos += len([i for i in line if i > 0])
        min_number = min(min_number, min(line))
        max_number = max(max_number, max(line))
        sum_all += sum(line)

records = {
    "count": count,
    "positive_count": count_pos,
    "min": min_number,
    "max": max_number,
    "sum": sum_all,
    "average": round(sum_all / count, 2) if count > 0 else 0.00
}        
with open(js, "w", encoding="UTF-8") as j:
    json.dump(records, j, ensure_ascii=False, indent=2)