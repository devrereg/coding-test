def solution(n):
    for x in range(1, n + 1):
        if n == x ** 2:
            return (x + 1) ** 2

    return -1


# 다른 풀이
def solution2(n):
    seq = n ** (1/2)

    if seq%1 == 0:
        return (seq + 1) ** 2
    return -1