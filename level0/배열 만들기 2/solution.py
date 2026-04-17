def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if str(i).replace('0','').replace('5','') == '':
            answer.append(i)
    if not answer:
        return [-1]
    return answer    

# 다른풀이
def solution2(l, r):
    answer = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1

    return [-1] if len(answer) == 0 else answer