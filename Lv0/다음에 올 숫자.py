def solution(common):
    n = common[1] - common[0]
    if common[2] == common[1] + n:
        answer = common[len(common)-1] + n
    else:
        n = common[1] // common[0]
        answer = common[len(common)-1] * n
    return answer