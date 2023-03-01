days = ['THU', 'FRI', 'SAT', 'SUN','MON', 'TUE', 'WED' ]
dates = [31,29,31,30,31,30,31,31,30,31,30,31]
def solution(a, b):
    date = 0
    for i in range(0, a-1):
        date += dates[i]
    date += b
    return days[(date)%7]
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12901