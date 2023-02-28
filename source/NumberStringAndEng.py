NumberWords = {"one":1, "two":2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}
def solution(s):
    for key in NumberWords.keys():
        print(key)
        s = s.replace(key, str(NumberWords.get(key)))
    return int(s)
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/81301