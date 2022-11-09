def solution(my_str, n):
    result = []
    
    #cnt 설정 == result값의 개수
    if len(my_str) % n == 0:
        cnt = len(my_str) // n
    else:
        cnt = len(my_str) // n + 1
    
    i=0
    f=0
    while i < cnt:
        result.append(my_str[f:f+n])
        i+=1
        f+=n
    return result