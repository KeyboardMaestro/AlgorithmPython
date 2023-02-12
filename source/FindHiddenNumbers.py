def solution(my_string):
    answer = 0
    temp = ''
    for ch in my_string:
        if ch.isnumeric():
            temp += ch
        else:
            if len(temp) != 0:
                answer += int(temp)
                temp = ''
    if len(temp) != 0:
        answer += int(temp)
        temp = ''
    return answer

# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120864