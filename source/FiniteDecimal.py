import math

def solution(a, b):
    gcm_divisor = gcd(a,b)
    b = b / gcm_divisor
    while b % 2 == 0 :
            b = b // 2
    while b % 5 == 0 :
            b = b // 5
    if b == 1:
        return 1
    else :
        return 2

def gcd(a, b):
    if b == 0 :
        return a
    bigger = max(a, b)
    smaller = min(a, b)
    rest = bigger % smaller
    return gcd(smaller, rest)

# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120878