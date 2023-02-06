def solution(n):
    answer = 0
    for i in range(4,n+1):
        if not isPrime(i):
            print(i)
            answer += 1
    return answer


def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120846