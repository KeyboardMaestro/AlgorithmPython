def solution(n):
    cursed = 0
    for i in range(0, n):
        cursed += 1
        cursed = isCursed(cursed)
    return cursed

def isCursed(number):
    while (('3' in str(number) or (number % 3 == 0))) :
        number += 1
    return number

# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120871