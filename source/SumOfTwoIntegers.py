def solution(a, b):
    if b < a :
        return sum(range(b, a+1))
    else:
        return sum(range(a,b+1))
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12912