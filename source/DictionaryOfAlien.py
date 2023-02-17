def solution(spell, dic):
    spell = set(spell)
    for dic1 in dic:
        if spell.issubset(set(dic1)):
            return 1
    return 2
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120869