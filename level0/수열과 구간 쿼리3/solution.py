def solution(arr, queries):
    for i,j in queries:
        i_val = arr[i]
        arr[i] = arr[j]
        arr[j] = i_val
    return arr

# 다른 풀이
def solution2(arr, queries):
    for l,r in queries:
        arr[l],arr[r] = arr[r],arr[l]