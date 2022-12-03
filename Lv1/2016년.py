def solution(a, b):
    answer = ''
    t = 0
    if a == 1:
        t = b
    elif a == 2:
        t = 31 + b
    elif a == 3:
        t = 60 + b
    elif a == 4:
        t = 91 + b
    elif a == 5:
        t = 121 + b
    elif a == 6:
        t = 152 + b
    elif a == 7:
        t = 182 + b
    elif a == 8:
        t = 213 + b
    elif a == 9:
        t = 244 + b
    elif a == 10:
        t = 274 + b
    elif a == 11:
        t = 305 + b
    elif a == 12:
        t = 335 + b
    if t % 7 == 0:
        answer = "THU"
    elif t % 7 == 1:
        answer = "FRI"
    elif t % 7 == 2:
        answer = "SAT"
    elif t % 7 == 3:
        answer = "SUN"
    elif t % 7 == 4:
        answer = "MON"
    elif t % 7 == 5:
        answer = "TUE"
    elif t % 7 == 6:
        answer = "WED"
    return answer