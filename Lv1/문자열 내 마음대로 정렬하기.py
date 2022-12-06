def solution(strings, n):
    answer = []
    a = []
    for i in strings:
        i = list(i)
        a.append(i[n])
    
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                tmp1 = a[i]
                a[i] = a[j]
                a[j] = tmp1
                
                tmp2 = strings[i]
                strings[i] = strings[j]
                strings[j] = tmp2
                
    for i in range(0,len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                if strings[i] > strings[j]:
                    tmp3 = strings[i]
                    strings[i] = strings[j]
                    strings[j] = tmp3
    return strings