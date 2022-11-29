def solution(price, money, count):
    answer = 0
    price_c = price
    sum = 0
    
    for i in range(0,count):
        sum += price
        price += price_c
    answer = sum - money
    
    if answer < 0:
        answer = 0
    return answer