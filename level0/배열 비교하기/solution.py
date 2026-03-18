def solution(arr1, arr2):
    result = 0
    if len(arr1) < len(arr2):
        result -= 1
    elif len(arr1) > len(arr2):
        result += 1
    else:
        if sum(arr1) != sum(arr2):
            result += -1 if sum(arr1) < sum(arr2) else 1

    return result


# 다른 풀이
def solution2(arr1, arr2):
    x, y = len(arr1), len(arr2)
    if x != y:
        return 1 if x > y else -1
    elif x == y:
        sum_x, sum_y = sum(arr1), sum(arr2)
        if sum_x > sum_y:
            return 1
        elif sum_x < sum_y:
            return -1
        else:
            return 0