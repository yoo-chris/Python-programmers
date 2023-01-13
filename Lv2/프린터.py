def solution(priorities, location):
    answer = 0
    queue = []
    index = []
    result = []
    for i in range(0,len(priorities)):
        queue.append(priorities[i])
        index.append(i)
    
    i = 0
    while len(result) != len(priorities):
        if i == len(priorities):
            i = 0
        if priorities[i] == max(priorities):
            priorities[i] = 0
            result.append(i)
            i += 1
        else:
            i += 1
            
    for i in range(0,len(result)):
        if result[i] == location:
            answer = i + 1
    return answer
