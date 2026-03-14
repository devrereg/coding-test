def solution(a, b):
    num1 = int(f'{a}{b}')
    num2 = int(f'{b}{a}')

    return num1 if num1 > num2 else num2


# 다른 풀이
def solution2(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))