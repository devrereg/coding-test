def solution(a, b):
    is_even_a = a % 2 == 1
    is_even_b = b % 2 == 1
    is_other_type = (a + b) % 2 == 1

    if is_even_a or is_even_b:
        return 2 * (a + b) if is_other_type else a ** 2 + b ** 2
    else:
        return abs(a - b)


# 다른풀이
def solution2(a, b):
    if a % 2 or b % 2:
        return 2 * (a + b) if (a + b) % 2 else a ** 2 + b ** 2
    else:
        return abs(a - b)
