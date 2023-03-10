def solution(n):
    answer = 0
    for i in range(2, n+1):
        for num in range(2,(i//2)+1):
            if i // num == 0:
                continue
        answer += 1
    return answer