def fragments(numbers):
    result = []
    i = 0
    while i < len(numbers) - 1:
        r = []
        r.append(numbers[i])
        while i < len(numbers) - 1 and numbers[i] < numbers[i + 1]:
            i += 1
            r.append(numbers[i])
        result.append(r)
        i += 1
    return result