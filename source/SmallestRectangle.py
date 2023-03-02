def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    w = max(width)
    h = max(height)
    return w * h
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/86491