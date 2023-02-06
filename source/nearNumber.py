def solution(array, n):
    data = []
    for i in array:
        data.append(abs(i-n))
    minumum = data.index(min(data))
    return array[minumum]
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120890