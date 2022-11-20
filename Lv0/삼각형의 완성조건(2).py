def solution(sides):
    answer = 0
    sides.sort()
    for i in range(1,sides[1]+1):
        if i + sides[0] > sides[1]:
            answer += 1
    for i in range(sides[1]+1, sides[0]+sides[1]):
        if i < sides[0] + sides[1]:
            answer += 1
    return answer