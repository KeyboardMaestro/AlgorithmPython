def solution(s):
    s = 'abcd'
    if not (len(s) == 4 or len(s) == 6):
        return False
    if not s.isnumeric():
        return False
    return True
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12918