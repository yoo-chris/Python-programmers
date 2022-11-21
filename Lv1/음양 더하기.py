def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1
    for i in absolutes:
        answer += i
    return answer