def solution(num_list, n):
    result = []

    for i in range(len(num_list)):
        if i % n == 0:
            result.append(num_list[i])

    return result


# 다른 풀이
def solution2(num_list, n):
    return num_list[::n]