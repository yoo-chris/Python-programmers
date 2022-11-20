def solution(score):
    answer = []
    score2 = []
    score3 = []
    result = []
    tmp = 0
    for i in range(1,len(score)+1):
        answer.append(i)
        
    for i in range(0,len(score)):
        score2.append(score[i][0]+score[i][1])
    
    for i in score2:
        score3.append(i)
    score3.sort(reverse=True)   #오름차순
    
    for i in range (1, len(score3)):
        if score3[i] == score3[i-1]:
            answer[i] = answer[i-1]
        
    for i in range(0,len(score2)):
        for j in range(0,len(score3)):
            if score2[i] == score3[j]:
                score3[j] = -1
                
                result.append(answer[j])
                break
    
    return result