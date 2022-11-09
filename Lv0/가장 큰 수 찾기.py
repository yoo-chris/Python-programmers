def solution(array):
    answer = []
    max = array[0]
    t = 0
    for i in range(1,len(array)):
        if array[i] > max:
            max = array[i]
            t = i
    answer.append(max)
    answer.append(t)
    return answer