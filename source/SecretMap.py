def solution(n, arr1, arr2):
    answer = []
    for idx in range(0, n):
        temp = ''
        for bit in str(bin(arr1[idx] | arr2[idx]))[2:]:
            if(bit == '1'):
                temp += '#'
            else:
                temp += ' '
        if(len(temp) < n):
            temp.join(' '*(n - len(temp)))
        answer.append(temp)
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/17681