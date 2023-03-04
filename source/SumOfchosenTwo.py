def solution(numbers):
    answer = []
    for idx,ele in enumerate(numbers):
        for i in range(idx+1,len(numbers)):
            answer.append(ele + numbers[i])
    return sorted(list(set(answer)))
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/68644