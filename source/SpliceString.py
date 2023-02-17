def solution(my_str, n):
    answer = []
    for index in range(0,(len(my_str)//n)+1):
        answer.append(my_str[index*n:(index*n)+n])
    if answer[-1] == "":
        answer.pop()
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120913