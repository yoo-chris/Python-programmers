def solution(s1, s2):
    answer = 0
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                answer += 1
    return answer