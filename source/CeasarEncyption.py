alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def solution(s, n):
    answer = ''
    for character in s:
        isUpper = False
        if character is ' ':
            answer += character
            continue
        if not(character in alphabet):
            isUpper = True
            character = character.lower()
        encode = alphabet.index(character)+n
        if encode >= 26:
            encode -= 26
        if isUpper:
            answer += alphabet[encode].upper()
        else:
            answer += alphabet[encode]
    return answer
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12926