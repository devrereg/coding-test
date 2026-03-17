def solution(arr, n):
    for index, num in enumerate(arr):
        if index % 2 != len(arr) % 2:
            arr[index] = num + n

    return arr

# 다른 풀이
def solution2(arr, n):
    for i in range(len(arr)):
        if i % 2 != len(arr) % 2:
            arr[i] += n
    return arr