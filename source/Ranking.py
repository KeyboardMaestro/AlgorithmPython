def solution(score):
    ranking = []
    rank = []
    for sc in score:
        rank.append(sum(sc))
    data = sorted(rank,reverse=True)
    for temp in rank:
        ranking.append(data.index(temp)+1)
    return ranking
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120882