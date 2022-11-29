def solution(sizes):
    answer = 0
    a = []
    b = []
    for i in range(0,len(sizes)):
        sizes[i].sort()
    for i in range(0,len(sizes)):
        a.append(sizes[i][0])
        b.append(sizes[i][1])
    a.sort()
    b.sort()
    
    answer = a[len(a)-1] * b[len(b)-1]
    return answer