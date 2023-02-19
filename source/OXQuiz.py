def solution(quizs):
    answer = []
    for quiz in quizs:
        value = 0
        polynomial = quiz.split(' ')
        if polynomial[1] == '-':
                value = int(polynomial[0]) - int(polynomial[2])
        else:
                value = int(polynomial[0]) + int(polynomial[2])
        print(value)
        if value == int(polynomial[4]):
            answer.append('O')
        else:
            answer.append('X')
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120907