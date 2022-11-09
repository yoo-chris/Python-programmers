def solution(array, height):
    answer = 0
    for i in range(0,len(array)):
        if array[i] > height:
            answer += 1
    return answer