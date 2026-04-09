def solution(arr):
    index_lst = [i for i in range(len(arr)) if arr[i] == 2]
    if len(index_lst) == 0:
        return [-1]

    return arr[min(index_lst) : max(index_lst)+1]


# 다른풀이
def solution2(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2): len(arr) - arr[::-1].index(2)]
