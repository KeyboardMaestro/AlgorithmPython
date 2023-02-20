def solution(num):
    trial = 0
    while num != 1:
        trial += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1
        if trial >= 500:
            return -1
    return trial
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12943