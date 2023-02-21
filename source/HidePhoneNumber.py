def solution(phone_number):
    return (len(phone_number[:-4])*'*')+phone_number[-4:]
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12948