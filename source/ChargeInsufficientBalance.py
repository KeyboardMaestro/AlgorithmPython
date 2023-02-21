def solution(price, money, count):
    count = (count * (count+1))/2
    if money-(price*count) < 0:
        return abs(money-(price*count))
    else:
        return 0
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/82612