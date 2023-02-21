def solution(arr):
    dupl = [arr[0]]
    for ele in arr:
        if not (ele == dupl[-1]):
            dupl.append(ele)
    return dupl
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3