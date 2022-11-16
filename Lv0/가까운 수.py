def solution(array, n):
    array.sort(reverse=True)
    answer = array[0]
    min = abs(array[0]-n)
    for i in array:
        if abs(i-n) <= min:
            min = abs(i-n)
            answer = i
    return answer