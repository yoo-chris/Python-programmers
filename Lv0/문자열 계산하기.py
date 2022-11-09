def solution(my_string):
    list = []
    list = my_string.split(" ")
    answer = int(list[0])
    for i in range(1, len(list)-1):
        if list[i] == '+':
            answer += int(list[i+1])
        elif list[i] == '-':
            answer -= int(list[i+1])
        else:
            continue
    return answer