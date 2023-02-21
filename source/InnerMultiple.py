def solution(a, b):
    answer = 0
    for bnum, anum in enumerate(a):
        answer += anum * b[bnum]
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/70128