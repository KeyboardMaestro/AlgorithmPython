def solution(str):
    answer = ''
    words = str.split(" ")
    for s in words:
        for i in range(0, len(s)):
            if i % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        answer += " "
    return answer.strip()
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12930