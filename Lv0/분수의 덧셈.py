def solution(denum1, num1, denum2, num2):
    answer = []
    up = 0
    down = 0
    down = num1 * num2
    up = denum1 * num2 + denum2 * num1
    
    for i in range(2,1000):
        while up % i == 0 and down % i == 0:
            up = up // i
            down = down // i
    answer.append(up)
    answer.append(down)
    return answer