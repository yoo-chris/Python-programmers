def solution(n):
    answer = 0
    sum = 0
    i = 1
    t = 1
    while t != n:
        
        sum += i
        i += 1
        
        if sum == n:
            sum = 0
            answer += 1
            t += 1
            i=t
            
        elif sum > n:
            sum = 0
            t += 1
            i=t
        
            
    return answer + 1