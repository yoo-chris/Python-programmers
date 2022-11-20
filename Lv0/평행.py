def solution(dots):
    answer = 0
    copy = []
    dots.sort()
    count = 0
    
    for i in range(0,len(dots)-1):
        for j in range(i+1, len(dots)):
            t = []
            t.append(dots[j][0] - dots[i][0])
            t.append(dots[j][1] - dots[i][1])
            copy.append(t)
    
    for i in range(0,len(copy)):
        for j in range(2, 101):
            if copy[i][0] % j == 0 and copy[i][1] % j == 0:
                copy[i][0] = copy[i][0] // j
                copy[i][1] = copy[i][1] // j
    copy.sort()
    for i in range(0,len(copy)-1):
        if copy[i] == copy[i+1]:
            count += 1
    
    if count > 0:
        answer = 1
    
    return answer