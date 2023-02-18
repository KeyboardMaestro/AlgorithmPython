def solution(keyinput, board):
    coordinate = [0, 0]
    limit = [board[0]//2, board[1]//2]
    for key in keyinput:
        if key[0] == 'r' and coordinate[0] < limit[0]:
            coordinate[0] += 1
        elif key[0] == 'l' and coordinate[0] > -limit[0]:
            coordinate[0] -= 1
        elif key[0] == 'u' and coordinate[1] < limit[1]:
            coordinate[1] += 1
        elif key[0] == 'd' and coordinate[1] > -limit[1]:
            coordinate[1] -= 1
    return coordinate
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120861