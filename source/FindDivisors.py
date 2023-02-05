def solution(n):
    answer = []
    for divisor in range(1, int(n/2+1)):
        if n % divisor == 0:
            answer.append(divisor)
    answer.append(n)
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120897