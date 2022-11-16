def solution(emergency):
    str1 = []         #emergency의 복사본
    answer = []       #실행 결과
    for i in emergency:
        str1.append(i)
    #주의 str1 = emergency로 복사해버리면 하나가 바뀔때 둘이 같이 바뀜
    
    str1.sort()
    for i in range(len(str1),0,-1):
        answer.append(i)
        
    for i in range(0,len(str1)):
        for j in  range(0,len(emergency)):
            if str1[i] == emergency[j]:
                tmp1 = str1[i]
                str1[i] = str1[j]
                str1[j] = tmp1
                    
                tmp2 = answer[i]
                answer[i] = answer[j]
                answer[j] = tmp2
    return answer