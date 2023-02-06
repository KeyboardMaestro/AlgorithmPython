def solution(num_list, n):
    answer = []
    index = 0
    temp = []
    level = 0
    for num in num_list:
        temp.append(num)
        index += 1
        if index == n:
            answer.append([])
            for i in temp:
                answer[level].append(i)
            index = 0
            temp.clear()
            level += 1
    print(answer)
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120842