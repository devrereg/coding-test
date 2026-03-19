def solution(arr):
    x = []
    for num in arr:
        x.extend([num]*num)
    return x


# 다른 풀이
def solution2(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer