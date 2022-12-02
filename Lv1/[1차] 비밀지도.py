def solution(n, arr1, arr2):
    answer = []
    a = []
    a_complete = []
    b = []
    b_complete = []
    
    #<arr1>
    for i in arr1:
        a.append(bin(i))
        
    for i in range(0,len(a)):
        c = ''
        if len(a[i]) != n+2:
            for k in range(0,n+2-len(a[i])):
                c += '0'
        for j in range(2,len(a[i])):
            c += a[i][j]
        a_complete.append(c)
        
    #<arr2>
    for i in arr2:
        b.append(bin(i))
    
    for i in range(0,len(b)):
        c = ''
        if len(b[i]) != n+2:
            for k in range(0,n+2-len(b[i])):
                c += '0'
        for j in range(2, len(b[i])):
            c += b[i][j]
        b_complete.append(c)
        
    for i in range(0,n):
        c = ''
        for j in range(0,n):
            if a_complete[i][j] == '0' and b_complete[i][j] == '0':
                c += ' '
            else:
                c += '#'
        answer.append(c)
            
    return answer
