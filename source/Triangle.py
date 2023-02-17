def solution(sides):
    possible = []
    edge = max(sides)
    for side in range(edge-1,edge):
        possible.append(side)

    for side in range(edge+1, sum(sides)):
        possible.append(side)
    return len(possible)
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120868