def solution(start_num, end_num):
    answer = []
    sum_value = end_num + start_num
    for num in range(end_num, start_num + 1):
        answer.append(sum_value - num)

    return answer



# 다른 풀이
def solution2(start, end):
    return list(range(start,end-1,-1))