def solution(n):
    answer = 0
    num = 1
    s = []
    
    while n > 0:
        s.append(n%3)
        n = n // 3
    
    for i in range(len(s)-1,-1,-1):
        answer += num * s[i]
        num *= 3
        
    return answer