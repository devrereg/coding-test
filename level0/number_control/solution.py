def solution(n, control):

    for c in control:
        if c == "w":
            n += 1
            continue
        if c == "s":
            n -= 1
            continue
        if c == "d":
            n +=10
            continue
        if c == "a":
            n -= 10
            continue

    return n

# 다른 풀이
def solution2(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer
