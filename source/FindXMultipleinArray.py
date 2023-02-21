def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    for ele in arr:
        if ele % divisor == 0:
            answer.append(ele)
    if len(answer) == 0:
        answer.append(-1)
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12910