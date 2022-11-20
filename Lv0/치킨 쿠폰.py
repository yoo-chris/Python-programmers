def solution(chicken):
    answer = 0
    service = 0
    coupon = chicken
    rest_coupon = 0
    while coupon // 10 > 0:
        answer += coupon // 10
        service = coupon // 10
        rest_coupon = coupon % 10
        coupon = service + rest_coupon
        
    return answer