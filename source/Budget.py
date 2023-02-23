def solution(d, budget):
    d = sorted(d)
    distribution = []
    for money in d:
        distribution.append(money)
        if sum(distribution) > budget:
            distribution.pop()
            break
    return len(distribution)
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12982