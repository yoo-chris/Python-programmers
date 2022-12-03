def solution(n, words):
    answer = []
    count = 0
    error = 100
    
    if len(words[0]) == 1:
        return [1,1]
    for i in range(1,len(words)):
        if (words[i][0] == words[i-1][len(words[i-1])-1]):
            count += 1
        else:
            error = i + 1
            break
            
        if words[i] in words[0:i]:
            error = i + 1
            break
        
        if len(words[i]) == 1:
            error = i + 1
            break
            
    if error == 100:
        answer.append(0)
        answer.append(0)
    else:
        if error % n == 0:
            answer.append(n)
            answer.append(error // n)
        else:
            answer.append(error % n)
            answer.append(error // n + 1)
            
    return answer