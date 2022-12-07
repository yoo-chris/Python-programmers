def solution(N, stages):
    answer = []
    rate = []
    stages.sort()
    k = 0
    count_m = len(stages)
    for i in range(1,N+1):
        count_s = 0
        #이 부분에서 실행시간 Down시켜야함
        for j in range(k,len(stages)):
            if stages[j] == i:
                k = j+1
                count_s += 1
        if count_m == 0:
            rate.append(0)
        else:
            rate.append(count_s / count_m)
        count_m = count_m - count_s
    
    i = 0
    t = 0
    while t != N:
        if rate[i] == max(rate):
            answer.append(i+1)
            rate[i] = -1
            i = -1
            t += 1
        i += 1
    
    return answer