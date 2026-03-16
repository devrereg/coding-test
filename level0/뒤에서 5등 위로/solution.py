def solution(num_list):
    num_list.sort()
    return num_list[5:]


# 다른풀이
def solution2(num_list):
    return sorted(num_list)[5:]