def solution(balls, share):
    if (balls == share) :
        return balls
    else :
        return facto(balls)/facto(balls-share)/facto(share)

def facto(number):
    if (number == 1):
        return 1
    else :
        return number * facto(number - 1)
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120840