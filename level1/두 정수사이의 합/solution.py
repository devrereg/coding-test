def solution(a, b):
    if a == b:
        return a
    cnt = abs(a-b)+1
    if cnt%2:
        return (a+b)*(cnt//2) + (a+b)//2
    else:
        return (a+b)*(cnt//2)

# 다른 풀이
def solution2(a, b):
    return sum(range(min(a, b), max(a, b) + 1))