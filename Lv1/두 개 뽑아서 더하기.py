def solution(numbers):
    answer = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1, len(numbers)):
            t = numbers[i] + numbers[j]
            if t in answer:
                continue
            else:
                answer.append(t)
    answer.sort()
    return answer