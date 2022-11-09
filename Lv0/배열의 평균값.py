def solution(numbers):
    answer = 0
    sum = 0
    for i in range(0,len(numbers)):
        sum += numbers[i]
    answer = sum / len(numbers)
    return answer