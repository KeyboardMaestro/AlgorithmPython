def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/42748