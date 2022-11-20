def solution(numlist, n):
    answer = []
    numlist.sort()
    f = -1
    
    for i in range(0,len(numlist)):
        min = 99999
        for j in range(0,len(numlist)):
            if abs(n - numlist[j]) <= min:
                min = abs(n - numlist[j])
                f= j
        answer.append(numlist[f])
        numlist[f] = 90000
    
    return answer