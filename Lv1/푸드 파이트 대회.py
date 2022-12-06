def solution(food):
    answer = ''
    list = ['0','1','2','3','4','5','6','7','8','9']
    
            
    for i in range(1,len(food)):
        answer += list[i]*(food[i]//2)
        
    answer += list[0]
    
    for i  in range(len(food)-1, 0, -1):
        answer += list[i]*(food[i]//2)
        
    return answer