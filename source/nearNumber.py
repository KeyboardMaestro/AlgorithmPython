def solution(array, n):
    data = []
    array = sorted(array)
    for i in array:
        data.append(abs(i-n))
    minimum = min(data)
    print(array)
    return array[data.index(minimum)]
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120890