import math


def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        sqrt = math.sqrt(n)
        return (sqrt+1) * (sqrt+1)
    else:
        return -1
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12934