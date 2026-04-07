def solution(arr, queries):
    for query in queries:
        for i in range(query[0], query[1] + 1):
            arr[i] += 1

    return arr



def solution2(arr, queries):
    for l,r in queries:
        for i in range(l,r+1): arr[i]+=1
    return arr