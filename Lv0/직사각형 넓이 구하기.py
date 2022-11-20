def solution(dots):
    answer = 0
    dots.sort()
    answer = abs(dots[0][1] - dots[1][1]) * abs(dots[1][0] - dots[2][0])
    return answer