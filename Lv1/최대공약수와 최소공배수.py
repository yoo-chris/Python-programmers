def solution(n, m):
    answer = []
    a=0 #최대공약수
    b=0 #최소공배수
    if n > m:
        tmp = n
        n = m
        m = tmp
    #최대 공약수 구하기
    for i in range(1, n+1):
        if (n% i == 0) and (m % i == 0):
            a = i;
    answer.append(a)
    
    #최소공배수 구하기
    for i in range(m, m*n+1):
        if i % n == 0 and i % m == 0:
            b = i;
            break
    answer.append(b)
    return answer