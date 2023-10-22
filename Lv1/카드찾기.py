def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_index = 0
    cards2_index = 0
    count = 0
    for i in range(0, len(goal)):
        if ((cards1_index < len(cards1)) and (goal[i] == cards1[cards1_index])):
            count += 1
            cards1_index += 1
            continue
            
        elif ((cards2_index < len(cards2)) and (goal[i] == cards2[cards2_index])):
            count += 1
            cards2_index += 1
            continue
        else:
            break
    if (count == len(goal)):
        answer = "Yes"
    else:
        answer = "No"
    return answer