def solution(arr, queries):
    for query in queries:
        s,e,k = query
        for i in range(len(arr)):
            if s <= i <= e and i % k == 0:
                arr[i] += 1                
    return arr


# 다른풀이
def solution2(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr