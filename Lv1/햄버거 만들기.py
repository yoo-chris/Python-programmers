def solution(ingredient):
    arr = []
    answer = 0
    for i in range(0,len(ingredient)):
        arr.append(ingredient[i])
        if arr[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(0, 4):
                arr.pop()
    return answer