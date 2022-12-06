def solution(lottos, win_nums):
    answer = []
    count_0 = 0             #0의 개수
    correct_num = 0         #번호중에 맞는것들 -> 최저순위
    
    for i in lottos:
        if i in win_nums:
            correct_num += 1
            
    for i in lottos:
        if i == 0:
            count_0 += 1
            
    
    if correct_num == 0:
        if count_0 == 0:
            answer.append(6) #최고순위
        else:
            answer.append(7 - correct_num - count_0) #최고순위
        answer.append(6) #최저순위
    else:
        answer.append(7 - correct_num - count_0) #최고순위
        answer.append(7 - correct_num) #최저순위
    return answer