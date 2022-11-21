def solution(a, b):
    answer = 0
    
    num = []
    num.append(a)
    num.append(b)
    num.sort()
    
    for i in range(num[0], num[1]+1):
        answer += i
    return answer