def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        value = a + d*i
        if included[i]: answer += value

    return answer

