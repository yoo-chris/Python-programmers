def solution(array, n):
    answer = 0
    for i in range(0,len(array)):
        if array[i] == n:
            answer += 1
    return answer