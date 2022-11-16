def solution(balls, share):
    answer = 0
    
    a=1
    b=1
    c=1
    
    for i in range(1,balls+1):
        a *= i
    for i in range(1,share+1):
        b *= i
    for i in range(1, (balls-share)+1):
        c *= i
        
    
    return a // (b * c)