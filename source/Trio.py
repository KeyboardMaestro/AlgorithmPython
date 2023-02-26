def solution(number):
    trio = 0
    for first in range(0, len(number)):
        for second in range(first+1, len(number)):
            for third in range(second+1, len(number)):
                if (number[first] + number[second] + number[third]) == 0:
                    trio += 1
    return trio
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/131705