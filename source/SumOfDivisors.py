def solution(left, right):
    answer = []
    for number in range(left, right+1):
        temp = []
        for divisor in range (1,number//2+1):
            if number % divisor == 0:
                temp.append(divisor)
        if (len(temp)+1) % 2 == 0:
            answer.append(number)
        else:
            answer.append(-number)
    return sum(answer)
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/77884