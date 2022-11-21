def solution(n):
    answer = 0
    num = []
    while n > 0:
        num.append(n%10)
        n = n // 10
    
    num.sort(reverse=True)
    
    for i in range(0,len(num)):
        answer *= 10
        answer += num[i]
    return answer