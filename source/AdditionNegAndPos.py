def solution(absolutes, signs):
    answer = 0
    for sign, num in enumerate(absolutes):
        if signs[sign] == False:
            answer -= num
        else:
            answer += num
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/76501