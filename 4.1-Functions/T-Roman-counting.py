def roman(a, b):
    d = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (9, 'IX'),
        (10, 'X'),
        (40, 'XL'),
        (50, 'L'),
        (90, 'XC'),
        (100, 'C'),
        (400, 'CD'),
        (500, 'D'),
        (900, 'CM'),
        (1000, 'M')
    ]
    result = []
    for s in [a, b, a + b]:
        r = ''
        for i, j in d[::-1]:
            if s // i == 1:
                r = r + j
                s = s % i
            elif s // i > 0:
                r = r + j * (s // i)
                s = s % i        
        result.append(r)
    return result[0] + ' + ' + result[1] + ' = ' + result[2]