def solution(arr1, arr2):
    for row in range(0,len(arr1)):
        for col in range(0, len(arr1[0])):
            arr1[row][col] = arr1[row][col] + arr2[row][col]
    return arr1
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/12950