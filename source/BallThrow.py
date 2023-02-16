def solution(numbers, k):
    index = 0
    for order in range(1,k):
        index += 2
        if index > (len(numbers)-1):
            index -= (len(numbers)-1)
    return numbers[index]
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120843