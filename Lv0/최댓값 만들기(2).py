def solution(numbers):
    answer = 0
    max = numbers[0]*numbers[1]
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i] * numbers[j] > max:
                max = numbers[i] * numbers[j]
    answer = max
    return answer