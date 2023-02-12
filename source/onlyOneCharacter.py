def solution(s):
    answer = ''
    alphabets = ['a','b','c','d','e','f','g','h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for alphabet in alphabets:
        if s.count(alphabet) == 1:
            answer += alphabet
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120896