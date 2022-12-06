def solution(k, m, score):
    answer = 0
    t = 0
    arr = []
    score.sort(reverse = True)
    #한 상자에 들어가는 사과의 수만큼 나눠서 배열을 만든다
    for a in range(0,len(score) // m + 1):
        a = []
        for i in range(0,m):
            if t == len(score):
                break
            a.append(score[t])
            t += 1
        arr.append(a)
    
    if len(arr[-1]) == 0:
        arr.pop()
    if len(arr[-1]) != m:
        arr.pop()
    
    for i in range(0,len(arr)):
        answer += arr[i][-1] * m
    return answer