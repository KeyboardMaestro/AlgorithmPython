def solution(numbers):
    numbers.sort()
    return max(numbers[len(numbers)-1]*numbers[len(numbers)-2], numbers[0] * numbers[1])
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120862