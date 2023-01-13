def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(0,len(progresses)):
        sum = progresses[i]
        count = 0
        while sum < 100:
            sum += speeds[i]
            count += 1
        days.append(count)
    
    a = days[0]
    count = 1
    for i in range(1, len(days)):
        if days[i] <= a:
            count += 1
        else:
            answer.append(count)
            a = days[i]
            count = 1
    answer.append(count)
    return answer