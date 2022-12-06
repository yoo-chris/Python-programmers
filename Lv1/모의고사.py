def solution(answers):
    answer = []
    s_1 = []
    s_2 = []
    s_3 = []
    t_1 = 1
    t_2 = 1
    t_3 = [3,1,2,4,5]
    s_3_cnt = 0
    k = 0
    cnt = [0,0,0]
    for i in range(0,len(answers)):
        #1번 수포자 배열 만들기
        s_1.append(t_1)
        if t_1 == 5:
            t_1 = 0
        t_1 += 1
        
        #2번 수포자 배열 만들기
        if i % 2 == 0:
            s_2.append(2)
        else:
            if t_2 == 2:
                t_2 += 1
            s_2.append(t_2)
            if t_2 == 5:
                t_2 = 0
            t_2 += 1
        
        #3번 수포자 배열 만들기
        s_3.append(t_3[k])
        s_3_cnt += 1
        if s_3_cnt == 2:
            k += 1
            s_3_cnt = 0
        if k == 5:
            k = 0
            
    for i in range(0,len(answers)):
        if answers[i] == s_1[i]:
            cnt[0] += 1
        if answers[i] == s_2[i]:
            cnt[1] += 1
        if answers[i] == s_3[i]:
            cnt[2] += 1
    
    for i in range(0,len(cnt)):
        if cnt[i] == max(cnt):
            answer.append(i+1)
            
    return answer