def solution(n):
    data = []
    for num in str(n):
        data.append(num)
    return int("".join(sorted(data, reverse=True)))
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12933