def solution(d, budget):
    answer = len(d)
    d.sort()
    sum = 0
    for i in range(0,len(d)):
        sum += d[i]
        if sum >= budget:
            answer = i
            break
    if sum == budget:
        answer += 1
    return answer