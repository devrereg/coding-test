def solution(start_num, end_num):
    answer = []
    for i in range(end_num - start_num + 1):
        answer.append(start_num + i)
    return answer


# 다른 풀이
def solution2(start_num, end_num):
    return list(range(start_num, end_num + 1))
