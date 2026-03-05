#
def solution(num_list, n):
    result = []
    for i in range(len(num_list) - (n - 1)):
        result.append(num_list[n - 1 + i])

    return result


# 모범 답안
def solution2(num_list, n, m):
    return num_list[n: m]


if __name__ == "__main__":
    print(solution([2, 1, 6], 3))
    print(solution2([5, 2, 1, 7, 5], 2,4))
