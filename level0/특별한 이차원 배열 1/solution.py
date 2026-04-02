def solution(n):
    answer = []
    for i in range(n):
        arr = []
        for j in range(n):
             arr.append(int(i == j))
        answer.append(arr)
    return answer

# 다른풀이
def solution2(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer
