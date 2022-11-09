def solution(num, k):
    answer = 0
    count = 0
    t = 0
    flag = 10   #왜 10인지 생각해보기
    while num > 0:
        t = num % 10
        if t == k:
            flag = count
        num = num // 10
        count += 1
    if flag == 10:
        answer = -1
    else:
        answer = count - flag
    return answer