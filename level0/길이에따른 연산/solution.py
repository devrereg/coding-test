def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)

    answer = 1
    for num in num_list:
        answer *= num

    return answer

# 다른풀이
from math import prod
def solution2(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)