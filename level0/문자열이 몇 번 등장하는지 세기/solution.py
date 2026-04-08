def solution(myString, pat):
    answer = 0
    pat_len = len(pat)

    for i in range(len(myString) - pat_len + 1):
        if pat == myString[i: pat_len + i]: answer += 1

    return answer


# 비슷하지만 다른풀이
def solution2(myString, pat):
    answer = 0

    for i in range(len(myString)):
        if myString[i:].startswith(pat) : answer += 1

    return answer