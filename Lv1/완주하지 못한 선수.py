def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = participant[len(participant)-1]
    
    for i in range(0,len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer