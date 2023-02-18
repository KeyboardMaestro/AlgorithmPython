def solution(chicken):
    coupon = chicken
    service = 0
    while coupon >= 10 :
        service += coupon//10
        service_coupon = coupon//10
        coupon = coupon % 10
        coupon += service_coupon
    return service
# Resource : https://school.programmers.co.kr/learn/courses/30/lessons/120884