def solution(lines):
    answer = 0
    a = []
    b = []
    for i in range(0,len(lines)):
        for j in range(lines[i][0], lines[i][1]):
            if j in a:
                if j in b:
                    continue
                else:
                    b.append(j)
            else:
                a.append(j)
            
    return len(b)