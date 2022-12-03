def solution(array, commands):
    answer = []
    for i in range(0,len(commands)):
        num = []
        for j in range(commands[i][0]-1, commands[i][1]):
            num.append(array[j])
        num.sort()
        answer.append(num[commands[i][2]-1])
    return answer