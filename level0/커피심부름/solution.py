def solution(order):
    prices = [5000 if "cafelatte" in menu else 4500 for menu in order]

    return sum(prices)

# 다른풀이
def solution2(order):
    return sum([5000 if "cafelatte" in menu else 4500 for menu in order])