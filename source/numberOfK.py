def solution(i, j, k):
    answer = 0
    for case in range(i, j+1):
        answer += str(case).count(str(k))
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120887?language=python3