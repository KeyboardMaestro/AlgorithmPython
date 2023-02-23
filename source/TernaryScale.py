def solution(n):
    exp = 0
    ternary = ''
    while n >= 3 ** (exp+1):
        exp += 1
    for exponent in range(exp, -1, -1):
        digit = n // (3 ** exponent)
        ternary += str(digit)
        n -= digit * (3 ** exponent)
    for exponent in range(0, exp+1):
        n += (3 ** exponent) * int(ternary[exponent])
    return n
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/68935