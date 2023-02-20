def solution(x, n):
    answer = []
    indexer = 1
    if x < 0:
        indexer = -1
    for number in range(x, x*n+indexer, x):
        answer.append(number)
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12954