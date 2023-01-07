def solution(s):
    str1 = '10 20 Z 30'
    answer = 0
    for a in str1.split():
        print(a)
        if a == 'Z' :
            answer -= temp
        else:
            answer += int(a)
            temp = int(a)
    return answer

def solution2(s):
    stack = []
    for sub in s.split():
        if sub == 'Z':
            stack.pop()
        else:
            stack.append(int(sub))
    return sum(stack)
