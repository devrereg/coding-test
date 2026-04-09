def solution(strArr):
    arr = []
    for s in strArr:
        arr.append(len(s))

    nums = set(arr)
    count_arr = []
    for num in nums:
        count_arr.append(len([i for i in arr if i == num]))

    return max(count_arr)



# 다른풀이
def solution2(strArr):
    return max(len(set(map(len, strArr))) for _ in strArr)



# 다른사람 풀이
def solution3(strArr):
    w_len = [0 for _ in range(31)]
    for w in strArr:
        w_len[len(w)] += 1
    return max(w_len)