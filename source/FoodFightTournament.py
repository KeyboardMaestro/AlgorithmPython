def solution(food):
    layout = ''
    for fdcode, fd in enumerate(food):
        for i in range (0, fd//2):
            layout += str(fdcode)
    layout += '0'
    return layout + layout[-2::-1]
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/134240