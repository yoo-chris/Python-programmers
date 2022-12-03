def solution(n):
    answer = 0
    
    f_n2 = 0
    f_n1 = 1
    sum = 0
    t = 0
    
    while t != n-1:
        
        sum = f_n2 + f_n1
        
        f_n2 = f_n1
        f_n1 = sum
        t += 1
        
    return sum % 1234567