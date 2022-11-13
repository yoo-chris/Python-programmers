def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for j in range (0,len(numbers)-1):
            answer.append(numbers[j])
    else:
        for j in range(1,len(numbers)):
            answer.append(numbers[j])
        answer.append(numbers[0])
        
    return answer