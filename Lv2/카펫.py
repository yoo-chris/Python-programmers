def solution(brown, yellow):
    answer = []
    num = (brown - 4) // 2
    for i in range(1,num):
        x = num - i
        y = i
        if x * y == yellow:
            answer.append(x+2)
            answer.append(y+2)
            break
    return answer