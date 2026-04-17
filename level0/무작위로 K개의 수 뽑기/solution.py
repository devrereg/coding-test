def solution(arr, k):
    answer = []
    for i, num in enumerate(arr):
        if not num in answer:
            answer.append(num)
            if len(answer) == k: break
        
    if len(answer) < k:
        answer += [-1]*(k-len(answer))
    return answer

# 다른풀이
def solution2(arr, k):
    answer = list(set(arr))[:k]
    if len(answer) < k:
        answer += [-1]*(k - len(answer))
        
    return answer

# 다른풀이
def solution3(arr, k):
    res = list(dict.fromkeys(arr))
    res.extend([-1] * max(0, k - len(res)))
    return res[:k]