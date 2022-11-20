def solution(polynomial):
    answer = ''
    s_polynomial = []
    x = []
    n = []
    s_polynomial = polynomial.split()
    a = 0
    b = 0
    
    for i in s_polynomial:
        if '+' in i:
            continue
        elif 'x' in i:
            x.append(i)
        else:
            n.append(i)
    
    for i in range(0,len(x)):
        if len(x[i]) == 1:
            x[i] = '1x'
            
    for i in range(0,len(x)):
        x[i] = x[i].replace('x','')
    
    #   ax+b
    for i in x:
        a += int(i)
    for i in n:
        b += int(i)
    
    if a == 0:
        if b == 0:
            answer += ''
        else:
            answer += str(b)
    else:
        if b == 0:
            if a != 1:
                answer += str(a)
            answer += 'x'
        else:
            if a != 1:
                answer += str(a)
            answer += 'x'
            answer += ' '
            answer += '+'
            answer += ' '
            answer += str(b)
            
    return answer