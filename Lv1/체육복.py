def solution(n, lost, reserve):
    answer = 0
    cloth = []
    #체육복을 다 가지고 있다고 가정
    for i in range(0,n+1):
        cloth.append(1)
        
    #체육복 잃어버린 학생들 -1
    for i in range(0,len(lost)):
        cloth[lost[i]] -= 1
        
    #여벌의 체육복을 가지고 있는 학생들 +1
    for i in range(0,len(reserve)):
        cloth[reserve[i]] += 1
    
    cloth.append(1)
    for i in range(1,n+1):
        if cloth[i] == 0:
            if cloth[i-1] == 2:
                cloth[i] += 1
                cloth[i-1] -= 1
                
            elif cloth[i+1] == 2:
                cloth[i] += 1
                cloth[i+1] -= 1
    
    for i in range(1,n+1):
        if cloth[i] != 0:
            answer += 1
    return answer