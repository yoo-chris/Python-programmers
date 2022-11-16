def solution(before, after):
    answer = 0
    before = ''.join(sorted(before))
    after = ''.join(sorted(after))
    if before == after:
        answer += 1
    return answer