def solution(n):
    divisor = 2
    while True:
        if (n % divisor == 1):
            break
        else:
            divisor += 1
    return divisor
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/87389