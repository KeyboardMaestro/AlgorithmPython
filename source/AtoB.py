def solution(before, after):
    alphabet = set(before)
    for char in alphabet:
        if before.count(char) != after.count(char):
            return 0
    return 1
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120886