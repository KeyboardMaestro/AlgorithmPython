def solution(numbers):
    number = { "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }
    for num in number:
        numbers = numbers.replace(num, str(number.get(num)))
    return int(numbers)
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120894