def solution(n):
    divisor = 2
    answer = {}
    while divisor <= n:
        if (n % divisor) == 0:
            n = n / divisor
            answer[divisor] = 0
        else:
            divisor += 1
    return list(answer.keys())
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120852