def solution(n):
    #규칙을 찾으면 매우 쉬움
    answer = 0
    a = 0
    b = 1
    for i in range(0, n):
        tmp = b
        b = a + b
        a = tmp
                
    
    return b % 1234567